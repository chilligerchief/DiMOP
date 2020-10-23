from flask_restful import Resource, reqparse
from Models.mat import MatModel
from flask import request


class MatPost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mat_desc',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_id_int',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_desc_int',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('cad_id',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mara_plast_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_rw',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('height',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('width',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('depth',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('unit',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('weight',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('weight_unit',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('volume',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('volume_unit',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('is_atomic',
                        type=bool,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('orga_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = MatPost.parser.parse_args()

        mat = MatModel(**data)
        mat.save_to_db()

        return {"message": "mat created successfully."}, 201


class Mat(Resource):
    def put(self, _id):
        data = MatPost.parser.parse_args()
        mat = MatModel.find_by_id(_id).first()
        if mat:
            mat.mat_desc = data['mat_desc']
            mat.mat_id_int = data['mat_id_int']
            mat.mat_desc_int = data['mat_desc_int']
            mat.cad_id = data['cad_id']
            mat.mara_plast_id = data['mara_plast_id']
            mat.mat_rw = data['mat_rw']
            mat.height = data['height']
            mat.width = data['width']
            mat.depth = data['depth']
            mat.unit = data['unit']
            mat.weight = data['weight']
            mat.weight_unit = data['weight_unit']
            mat.volume = data['volume']
            mat.volume_unit = data['volume_unit']
            mat.is_atomic = data['is_atomic']
            mat.orga_id = data['orga_id']

            mat.save_to_db()
        return {'mat': 'mat updated successfully'}

    def delete(self, _id):
        mat = MatModel.find_by_id(_id).first()
        if mat:
            mat.delete_from_db()
        return {'mat': 'mat deleted successfully'}


class MatGet(Resource):
    def get(self):
        args = request.args
        if "orga_id" in args:
            mat = MatModel.find_by_orga_id(args["orga_id"])
        elif "cons_id" in args:
            mat = MatModel.find_by_cons_id(args["cons_id"])
        my_list = []
        for x in mat:
            my_list.append(dict(x))
        return my_list
