from flask_restful import Resource, reqparse
from dbfunctions.connect import db
from sqlalchemy import text

class Tabletree(Resource):
    def get(self, mast_id):
        full_list = []
        mast_ids = [mast_id]
        while mast_ids:
            mast_id = mast_ids.pop()
            temp = [dict(x) for x in findchildren(mast_id)]
            full_list += temp
            mast_ids += [t["mast_id_children"] for t in temp if t["mast_id_children"] != None]
        return full_list

def findchildren(mast_id):
    sql = text("SELECT stpo.mast_id AS mast_id_parent, stpo.mara_id, mara.mara_nr, mara.mat_desc, stpo.pos, mast.id AS mast_id_children, stpo.height_erp, stpo.width_erp, stpo.depth_erp, stpo.unit_erp, stpo.volume_cad, stpo.unit_cad, stpo.weight_ui, stpo.qr_relevant FROM stpo left join mast ON stpo.mara_id=mast.mara_id LEFT JOIN mara ON mast.mara_id=mara.id WHERE stpo.mast_id=:mast_id")
    result = db.session.execute (sql, params={"mast_id": mast_id})
    return result.fetchall()
