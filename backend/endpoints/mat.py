# author: topr
# last updated: 02.12.2020
# currently used: yes
# description: is used to manage materials (parts that either can have components below
# (if is_atomic == false) or plastics (if is_atomic == true))

from Models.mat import MatModel
from flask_restful import Resource, reqparse, request
from dbfunctions.connect import db
from sqlalchemy import create_engine, MetaData, text
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


class MatPost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mat_desc',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_id_int',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_desc_int',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('cad_id',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mara_plast_id',
                        type=int,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_rw',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('height',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('width',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('depth',
                        type=float,
                        required=False,
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
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('volume_unit',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('is_atomic',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('orga_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('cons_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('del_kz',
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
            mat.mara_plast_id = data['mara_plast_id']

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


class MatGetNew(Resource):
    def get(self):
        db_connection_str = 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop'
        db = create_engine(db_connection_str)

        mat = pd.read_sql_table('mat', db)

        newest_mat = mat["id"][mat.shape[0]-1]

        return newest_mat
