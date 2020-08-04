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
    perp = db.relationship('PerpModel', lazy='dynamic')
    #perp = db.relationship('PerpModel', backref=db.backref('kons'), primaryjoin='KonsModel.id == PerpModel.kons_id')


    def __init__(self, kons_title, kons_desc, orga_id, mara_id, del_kz, created_at=None, updated_at=None):
        self.kons_title = kons_title
        self.kons_desc = kons_desc
        self.orga_id = orga_id
        self.mara_id = mara_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.del_kz = del_kz

    ### GET, POST; PUT; DELETE
    def json(self):
        return { 'id' : self.id, 'kons_title' : self.kons_title, 'kons_desc' : self.kons_desc, 'orga_id' : self.orga_id, 'mara_id' : self.mara_id, 'del_kz' : self.del_kz}

    #@classmethod
    #def find_by_user_id(cls, user_id):
        #return cls.query().join(cls.perp, cls._id == cls.perp.kons_id).filter_by(userid=cls.perp.user_id).all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id)


    #### POST PUT

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    #def get_from_db(self):
        #db.session.execute(self)