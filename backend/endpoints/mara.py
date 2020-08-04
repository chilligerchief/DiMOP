from flask_restful import Resource, reqparse
from Models.mara import MaraModel

class MaraGet(Resource):
    def get(self, user_id):
        mara = MaraModel.find_by_user_id(user_id)
        if mara:
            return {'Materialien': [x.json() for x in mara.all()]}
        else:
            return {'mara': 'material not found'}, 404

