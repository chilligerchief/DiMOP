from flask_restful import Resource, reqparse
from Models.BomItem import BomItemModel

class BomItemGet(Resource):
    def get(self, mast_id):
        bomitem = BomItemModel.find_by_mast_id(mast_id)
        my_list = []
        for x in bomitem:
            my_list.append(dict(x))
        return my_list

