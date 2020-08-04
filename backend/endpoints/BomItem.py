from flask_restful import Resource, reqparse
from Models.BomItem import BomItemModel

class BomItemGet(Resource):
    def get(self, mast_id):
        bomitem = BomItemModel.find_by_mast_id(mast_id)
        if bomitem:
            return {'Stücklistenitems': [x.json() for x in bomitem.all()]}
        else:
            return {'bomitem': 'Item not found'}, 404

