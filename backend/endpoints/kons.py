from flask_restful import Resource, reqparse
from Models.kons import KonsModel
import hashlib, uuid
from datetime import datetime


class UserRegister(Resource):
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
                        help="This field is optional, but a real Name should be used ;)."
                        )
    parser.add_argument('mara_id',
                        type=int,
                        required=True,
                        help="This field is optional, but a real Name should be used ;)."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        password = data["password"]

        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        data["password"] = hashed_password
        data["pw_salt"] = salt

        if UserModel.find_by_e_mail(data["e_mail"]):
            return {"message": "A user with that e_mail already exists"}, 400

        user = UserModel(**data)  # (data["e_mail"], data["password"])
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class DimopUser(Resource):
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
                        help="This field is optional, but a real Name should be used ;)."
                        )
    parser.add_argument('mara_id',
                        type=int,
                        required=True,
                        help="This field is optional, but a real Name should be used ;)."
                        )

    def get(self, _id):
        user = UserModel.find_by_id(_id)
        if user:
            return user.json()
        else:
            return {'user': 'User not found'}, 404

    def put(self, _id):
        data = DimopUser.parser.parse_args()

        user = UserModel.find_by_id(_id)
        update_user = {"firstname": data["firstname"]}
        # "id": data["_id"],'surname': data['surname'], 'orga_id': data['orga_id'], 't_function_id': data['t_function_id'], 'updated_at': datetime, 'del_kz': data["del_kz"]
        if user:
            try:
                UserModel.update(update_user)
            except:
                return {"message": "An error occurred updating the DimopUser."}, 500

        return update_user

    def delete(self, _id):
        user = UserModel.find_by_id(_id)
        if user:
            user.delete_from_db()
        return {'user': 'User deleted'}


#class Users(Resource):
#   def get(self):
#        return {'users': [user.json() for user in UserModel.query.all()]}
