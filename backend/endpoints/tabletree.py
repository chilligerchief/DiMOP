from flask_restful import Resource, reqparse
from dbfunctions.connect import db
from sqlalchemy import create_engine, MetaData, text
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np


class Tabletree(Resource):
    def get(self, mat_id):

        db = connect_db()

        mat = pd.read_sql_table('mat', db)
        bom = pd.read_sql_table('bom', db)

        result_list = []
        result = [1, None]

        result_df = mat.loc[mat["id"] == mat_id]

        for col in result_df.columns:
            result.append(result_df[col].item())

        result_list.append(result)

        result_list = getChildren(mat_id, result_list, mat, bom)

        result_df = pd.DataFrame(result_list).fillna(
            np.nan).replace([np.nan], [None])

        result_df = result_df.rename(
            columns={0: "result_id", 1: "parent_id", 2: "mat_id", 3: "mat_desc", 4: "mat_id_int", 5: "mat_desc_int", 6: "cad_id", 7: "mara_plast_id", 8: "mat_rw", 9: "height", 10: "width", 11: "depth", 12: "unit", 13: "weight", 14: "weight_unit", 15: "volume", 16: "volume_unit", 17: "is_atomic", 18: "orga_id"})

        result_json = result_df.to_dict(orient="records")

        return result_json


def connect_db():
    db_connection_str = 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop'
    db_connection = create_engine(db_connection_str)

    return db_connection


def addResult(child, parent_id, result_list, mat):

    result_df = mat.loc[mat["id"] == child]

    result = [result_list[len(result_list)-1][0]+1, parent_id]

    for col in result_df.columns:
        result.append(result_df[col].item())

    result_list.append(result)

    return result_list


def getChildren(mat_id, result_list, mat, bom):

    bom_entry = bom.loc[bom["parent_mat_id"] == mat_id]

    if(len(bom_entry) != 0):

        children = bom.loc[bom["parent_mat_id"] == mat_id]["mat_id"].tolist()

        parent_id = result_list[len(result_list)-1][0]

        for child in children:
            addResult(child, parent_id, result_list, mat)
            getChildren(child, result_list, mat, bom)

    else:
        print(F"{mat_id} has no children")

    return result_list
