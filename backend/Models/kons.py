from dbfunctions.connect import db
from datetime import datetime

class KonsModel(db.Model):
    __tablename__ = 'kons'

    id = db.Column(db.Integer, primary_key=True)
    kons_title = db.Column(db.String(255))
    kons_desc = db.Column(db.Text(65535))
    orga_id = db.Column(db.Integer) #db.ForeignKey('orga_id.id')
    mara_id = db.Column(db.Integer) #db.ForeignKey('mara_id.id')
    created_at = datetime
    updated_at = datetime
    del_kz = db.Column(db.Boolean)


    def __init__(self, kons_title, kons_desc, orga_id, mara_id, created_at=None, updated_at=None, del_kz=None):
        self.kons_title = kons_title
        self.surname = kons_desc
        self.orga_id = orga_id
        self.mara_id = mara_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.del_kz = del_kz

    ### GET, POST; PUT; DELETE
    def json(self):
        return { 'id' : self.id, 'kons_title' : self.kons_title, 'kons_desc' : self.kons_desc, 'orga_id' : self.orga_id, 'mara_id' : self.mara_id, 'del_kz' : self.del_kz}


    @classmethod
    def find_by_userid(cls, userid):
       # query = ('SELECT kons.id, kons.kons_title, kons.kons_desc, orga.orga_name, mara.mara_nr, mara.mat_desc, kons.created_at, kons.updated_at, kons.del_kz FROM kons LEFT JOIN mara ON kons.mara_id=mara.id LEFT join orga ON kons.orga_id=orga.id LEFT JOIN perp on perp.kons_id=kons.id LEFT JOIN user on perp.user_id=user.id WHERE user.id='"+ userid + "'")

        #return cls.query.filter_by(surname=surname).first()

    @classmethod
    def find_by_e_mail(cls, e_mail):
        return cls.query.filter_by(e_mail=e_mail).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    #### POST PUT

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()