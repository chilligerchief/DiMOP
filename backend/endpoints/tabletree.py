from flask_restful import Resource, reqparse
from dbfunctions.connect import db
from sqlalchemy import text

class Tabletree(Resource):
    def get(self, mast_id):
        tree = findchildrean(mast_id)
        my_list = []
        for x in tree:
            my_list.append(dict(x))
        return my_list

def findchildrean(mast_id):
    sql = text("SELECT stpo.mast_id, stpo.mara_id, stpo.pos, mast.id AS mast_id_childrean FROM stpo left join mast ON stpo.mara_id=mast.mara_id WHERE stpo.mast_id=:mast_id")
    result = db.session.execute (sql, params={"mast_id": mast_id})
    return result.fetchall()