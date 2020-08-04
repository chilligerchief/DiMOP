from flask import jsonify
from flask_restful import Resource, reqparse
from Models.kons import KonsModel
from dbfunctions.connect import db
import hashlib, uuid


class KonsPost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('kons_title',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('kons_desc',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('orga_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mara_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('del_kz',
                        type=bool,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = KonsPost.parser.parse_args()

        kons = KonsModel(**data)
        kons.save_to_db()

        return {"message": "Kons created successfully."}, 201


class Kons(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('kons_title',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('kons_desc',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def put(self, _id):
        data = Kons.parser.parse_args()
        kons = KonsModel.find_by_id(_id).first()
        if kons:
            kons.kons_title = data['kons_title']
            kons.kons_desc = data['kons_desc']
            kons.save_to_db()
        return {'kons': 'Kons updated successfully'}

    def delete(self, _id):
        kons = KonsModel.find_by_id(_id).first()
        if kons:
            kons.delete_from_db()
        return {'kons': 'Kons deleted successfully'}

class KonsGet(Resource):
    def get(self, _id):
        kons = KonsModel.find_by_id(_id).first()
        if kons:
            return kons.json()
        else:
            return {'kons': 'kons not found'}, 404

class TestKonsGet(Resource):
    def get(self):
        query = db.session.execute('Select * from kons')
        return {'Konstruktionen': [x.json() for x in query]}