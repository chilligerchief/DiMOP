from flask_restful import Resource, reqparse
from Models.BomAl import BomAlModel

class BomAlGet(Resource):
    def get(self, kons_id):
        bomal = BomAlModel.find_by_kons_id(kons_id)
        my_list = []
        for x in bomal:
            my_list.append(dict(x))
        return my_list
