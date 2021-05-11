"""
author: topr
last updated: 11.05.2021
currently used: yes
description: used to import data
"""

from Models.rel import RelModel
from flask_restful import Resource, reqparse
from dbfunctions.connect import connect_db
from sqlalchemy import create_engine, MetaData, text
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


class Import(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)

        return "Everything worked just fine!"
