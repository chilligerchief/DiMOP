from flask_restful import Resource, reqparse
from Models.mara import MaraModel

class MaraGet(Resource):
    def get(self, user_id):
        mara = MaraModel.find_by_user_id(user_id)
        my_list = []
        for x in mara:
            my_list.append(dict(x))
        return my_list

