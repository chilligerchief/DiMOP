from flask_restful import Resource, reqparse
from Models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('e_mail',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('firstname',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_e_mail(data["e_mail"]):
            return {"message": "A user with that e_mail already exists"}, 400

        user = UserModel(**data) #(data["e_mail"], data["password"])
        user.save_to_db()

        return {"message": "User created successfully."}, 201