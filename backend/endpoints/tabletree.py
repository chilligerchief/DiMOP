"""
author: topr
last updated: 12.12.2020
currently used: yes
description: used to create the bill of material in a tree structure

Needs more description of what is going on.

"""

from flask_restful import Resource, reqparse
from dbfunctions.connect import connect_db
from sqlalchemy import create_engine, MetaData, text
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np


class Tabletree(Resource):

    # main function that assembles table tree of a given mat_id
    def get(self, mat_id):
        db = connect_db()
        mat = pd.read_sql_query('SELECT * FROM mat', db)
        bom = pd.read_sql_query('SELECT * FROM bom', db)

        result_list = []
        result = [None, 1, None]

        result_df = mat.loc[mat["id"] == mat_id]

        for col in result_df.columns:
            result.append(result_df[col].item())

        result_list.append(result)

        result_list = getChildren(mat_id, result_list, mat, bom)

        result_df = pd.DataFrame(result_list).fillna(
            np.nan).replace([np.nan], [None])

        result_df = result_df.rename(
            columns={
                0: "bom_id",
                1: "result_id",
                2: "parent_id",
                3: "mat_id",
                4: "mat_desc",
                5: "mat_id_int",
                6: "mat_desc_int",
                7: "cad_id",
                8: "mara_plast_id",
                9: "mat_rw",
                10: "height",
                11: "width",
                12: "depth",
                13: "unit",
                14: "weight",
                15: "weight_unit",
                16: "volume",
                17: "volume_unit",
                18: "is_atomic",
                19: "orga_id",
                20: "cons_id"})

        # To catch materials that have no components and are not atomic
        try:
            result_df = getBomLevel(result_df)
        except:
            result_df["level"] = 1

        plast_list = list(set(result_df.loc[(result_df["mara_plast_id"] != "None") & (
            result_df["mara_plast_id"].notna())]["mara_plast_id"].tolist()))
        print(plast_list)
        plast_desc, plast_family = [], []

        for element in plast_list:
            sql = F"SELECT mat_desc, campus_fam FROM plast WHERE id = {int(element)}"
            result = db.execute(sql).fetchall()
            plast_desc.append(result[0][0])
            plast_family.append(result[0][1])

        plast_tuples = list(zip(plast_list, plast_desc, plast_family))

        df_plast = pd.DataFrame(plast_tuples, columns=[
                                'p_id', 'plast_desc', 'plast_fam'])

        df_plast["p_id"] = df_plast["p_id"].astype(str)
        result_df["mara_plast_id"] = result_df["mara_plast_id"].astype(
            str)

        # print(df_plast.dtypes)
        # print(result_df.dtypes)

        df_merged = pd.merge(result_df, df_plast, left_on='mara_plast_id',
                             right_on='p_id', how='left').drop('p_id', axis=1)

        df_merged = df_merged.fillna(np.nan).replace([np.nan], [None])

        result_json = df_merged.to_dict(orient="records")

        return result_json

# connects to database


# def connect_db():
#     db_connection_str = 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop'
#     db_connection = create_engine(db_connection_str)

#     return db_connection

# adds result (tuple) to result list


def addResult(child, parent_id, result_list, mat, child_bom_entry):

    result_df = mat.loc[mat["id"] == child]

    result = [child_bom_entry, result_list[len(result_list)-1][1]+1, parent_id]

    for col in result_df.columns:
        result.append(result_df[col].item())

    result_list.append(result)

    return result_list

# get children for given mat_id


def getChildren(mat_id, result_list, mat, bom):

    bom_entry = bom.loc[bom["parent_mat_id"] == mat_id]

    if(len(bom_entry) != 0):

        children = bom.loc[bom["parent_mat_id"] == mat_id]["mat_id"].tolist()
        children_bom_entries = bom.loc[bom["parent_mat_id"]
                                       == mat_id]["id"].tolist()

        parent_id = result_list[len(result_list)-1][1]

        for child, child_bom_entry in zip(children, children_bom_entries):
            addResult(child, parent_id, result_list, mat, child_bom_entry)
            getChildren(child, result_list, mat, bom)

    else:
        print(F"{mat_id} has no children")

    return result_list

# Subfunction for getBomLevel


def getLevels(dictionary, depth_list, start=0):

    for key, value in dictionary.items():
        depth_list.append(start + 1)
        if isinstance(value, dict):
            getLevels(value, depth_list, start=start+1)

    return depth_list


# Gets bom level (depth) of each component
def getBomLevel(df):

    parent_child_pairs = []

    for parent, child in zip(df["parent_id"].to_list(), df["result_id"].to_list()):
        parent_child_pairs.append((parent, child))

    parent_child_pairs = parent_child_pairs[1:]

    graph = {name: set() for tup in parent_child_pairs for name in tup}
    has_parent = {name: False for tup in parent_child_pairs for name in tup}
    for parent, child in parent_child_pairs:
        graph[parent].add(child)
        has_parent[child] = True

    roots = [name for name, parents in has_parent.items() if not parents]

    def traverse(hierarchy, graph, names):
        for name in names:
            hierarchy[name] = traverse({}, graph, graph[name])
        return hierarchy

    nested_parent_child_dict = traverse({}, graph, roots)

    levels = getLevels(nested_parent_child_dict, depth_list=[])
    df["level"] = levels

    return df
