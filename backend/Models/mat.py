from dbfunctions.connect import db
from sqlalchemy import text


class MatModel(db.Model):
    __tablename__ = 'mat'

    id = db.Column(db.Integer, primary_key=True)
    mat_desc = db.Column(db.String)
    mat_id_int = db.Column(db.String)
    mat_desc_int = db.Column(db.String)
    cad_id = db.Column(db.String)
    mara_plast_id = db.Column(db.Integer)
    mat_rw = db.Column(db.Float)
    height = db.Column(db.Float)
    width = db.Column(db.Float)
    depth = db.Column(db.Float)
    unit = db.Column(db.String)
    weight = db.Column(db.Float)
    weight_unit = db.Column(db.String)
    volume = db.Column(db.Float)
    volume_unit = db.Column(db.String)
    is_atomic = db.Column(db.Boolean)
    orga_id = db.Column(db.Integer)

    def __init__(self, mat_desc, mat_id_int, mat_desc_int, cad_id, mara_plast_id, mat_rw, height, width, depth, unit, weight, weight_unit, volume, volume_unit, is_atomic, orga_id):

        self.mat_desc = mat_desc
        self.mat_id_int = mat_id_int
        self.mat_desc_int = mat_desc_int
        self.cad_id = cad_id
        self.mara_plast_id = mara_plast_id
        self.mat_rw = mat_rw
        self.height = height
        self.width = width
        self.depth = depth
        self.unit = unit
        self.weight = weight
        self.weight_unit = weight_unit
        self.volume = volume
        self.volume_unit = volume_unit
        self.is_atomic = is_atomic
        self.orga_id = orga_id

    def json(self):
        return {'id': self.id,
                'mat_desc': self.mat_desc, 'mat_id_int': self.mat_id_int, 'mat_desc_int': self.mat_desc_int, 'cad_id': self.cad_id, 'mara_plast_id': self.mara_plast_id, 'mat_rw': self.mat_rw, 'height': self.height, 'width': self.width, 'depth': self.depth,
                'unit': self.unit, 'weight': self.weight, 'weight_unit': self.weight_unit, 'volume': self.volume, 'volume_unit': self.volume_unit, 'is_atomic': self.is_atomic, 'orga_id': self.orga_id
                }

    @classmethod
    def find_by_orga_id(cls, orga_id):
        sql = text("SELECT * FROM mat WHERE mat.orga_id=:orga_id")
        result = db.session.execute(sql, params={"orga_id": orga_id})
        return result.fetchall()

    @classmethod
    def find_by_cons_id(cls, cons_id):
        sql = text(
            "SELECT * FROM mat LEFT JOIN mat_cons ON mat_cons.mat_id=mat.id WHERE mat_cons.cons_id=:cons_id")
        result = db.session.execute(sql, params={"cons_id": cons_id})
        return result.fetchall()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
