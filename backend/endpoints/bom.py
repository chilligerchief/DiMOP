# author: topr
# last updated: 05.11.2020
# currently used: yes
# description: used to get, add and delete bom entries

from flask_restful import Resource, reqparse
from Models.bom import BomModel

class Bom(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("mat_id",
                        type=int,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument("parent_mat_id",
                        type=int,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        data = Bom.parser.parse_args()

        bom = BomModel(**data)
        bom.save_to_db()

        return {"bom": "entry created successfully."}, 201

        return {bom}

    def get(self):
        bom = BomModel.find_all()
        my_list = []
        for x in bom:
            my_list.append(dict(x))
        return my_list


class BomAlter(Resource):
    def delete(self, _id):
        bom = BomModel.find_by_id(_id).first()
        if bom:
            bom.delete_from_db()
        return {"bom": "material deleted successfully"}
