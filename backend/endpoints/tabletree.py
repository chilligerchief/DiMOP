from flask_restful import Resource, reqparse
from dbfunctions.connect import db
from sqlalchemy import create_engine, MetaData, text
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


class Tabletree(Resource):
    def get(self, mara_id):

        db = connect_db()

        mara_fert = pd.read_sql_table('mara_fert', db)
        stpo = pd.read_sql_table('stpo', db)

        result_list = []
        result = [1, 0]

        result_df = mara_fert.loc[mara_fert["id"] == mara_id]

        for col in result_df.columns:
            result.append(result_df[col].item())

        result_list.append(result)

        result_list = getChildren(mara_id, result_list, mara_fert, stpo)

        result_df = pd.DataFrame(result_list)
        result_df = result_df.rename(
            columns={0: "result_id", 1: "parent_id", 2: "mara_fert_id", 3: "mat_desc", 4: "mat_id_int", 5: "mat_desc_int", 6: "cad_id", 7: "mara_plast_id", 8: "mat_rw", 9: "height", 10: "width", 11: "depth", 12: "unit", 13: "weight", 14: "weight_unit", 15: "volume", 16: "volume_unit"})

        result_json = result_df.to_json(orient="records")

        return result_json


def connect_db():
    db_connection_str = 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop'
    db_connection = create_engine(db_connection_str)

    return db_connection


def addResult(child, parent_id, result_list):

    result_df = mara_fert.loc[mara_fert["id"] == child]

    result = [result_list[len(result_list)-1][0]+1, parent_id]

    for col in result_df.columns:
        result.append(result_df[col].item())

    result_list.append(result)

    return result_list


def getChildren(mara_id, result_list, mara_fert, stpo):

    stpo_entry = stpo.loc[stpo["parent_mara_id"] == mara_id]

    if(len(stpo_entry) != 0):

        children = stpo.loc[stpo["parent_mara_id"]
                            == mara_id]["mara_id"].tolist()

        parent_id = result_list[len(result_list)-1][0]

        for child in children:
            addResult(child, parent_id, result_list)
            getChildren(child, result_list, mara_fert, stpo)

    else:
        print(F"{mara_id} has no children")

    return result_list
