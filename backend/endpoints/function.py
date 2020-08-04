import sqlalchemy
from flask import jsonify
from flask_restful import Resource, reqparse
from Models.function import FunctionModel
from dbfunctions.connect import db

class Function(Resource):
    def get(self):
        query = sqlalchemy.text('Select * from t_function')
        return {'Funktionen': [x.json() for x in FunctionModel.query.all()]}