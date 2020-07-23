from flask_restful import Resource, reqparse
from Models.function import FunctionModel

class Function(Resource):
    def get(self):
        return {'function': [function.json() for function in FunctionModel.query.all()]}