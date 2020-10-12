from flask_restful import Resource, reqparse
from dbfunctions.connect import db
from sqlalchemy import create_engine, MetaData, text
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


class Tabletree(Resource):
    def get(self, mara_id):

        db = connect_db()

        mast, stpo = loadTables(db)

        result_list = []
        result = [mara_id, 1, 0]
        result_list.append(result)
        result_list = getChildren(mara_id, result_list, mast, stpo)

        return result_list


def connect_db():
    db_connection_str = 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop'
    db_connection = create_engine(db_connection_str)

    return db_connection


def loadTables(db):

    print("SQL request")
    # mast - table with materials that have children
    mast = pd.read_sql_table('mastTobi', db)

    # stpo - table with bom (bill of materials) positions
    stpo = pd.read_sql_table('stpoTobi', db)

    return mast, stpo


def addResult(child, parent_id, result_list):

    result = [child, result_list[len(result_list)-1][1]+1, parent_id]
    result_list.append(result)

    return result_list


def getChildren(mara_id, result_list, mast, stpo):

    mast_entry = mast.loc[mast["mara_id"] == mara_id]["id"]

    if(len(mast_entry)):
        mast_id = mast_entry.item()
        children = stpo.loc[stpo["mast_id"] == mast_id]["mara_id"].tolist()

        parent_id = result_list[len(result_list)-1][1]

        for child in children:
            addResult(child, parent_id, result_list)
            getChildren(child, result_list, mast, stpo)

    else:
        print(F"{mara_id} has no mast entry")

    return result_list
