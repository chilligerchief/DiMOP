from flask_restful import Resource, reqparse
from Models.BomAl import BomAlModel

class BomAlGet(Resource):
    def get(self, kons_id):
        bomal = BomAlModel.find_by_kons_id(kons_id)
        if bomal:
            return {'Stücklistenalternativen': [x.json() for x in bomal.all()]}
        else:
            return {'bomal': 'bom alternative not found'}, 404
