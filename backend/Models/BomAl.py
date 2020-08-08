from dbfunctions.connect import db
from datetime import datetime
from sqlalchemy import text

class BomAlModel(db.Model):
    __tablename__ = 'mast'

    id = db.Column(db.Integer, primary_key=True)
    bom_nr = db.Column(db.Integer)
    bom_al = db.Column(db.Integer)
    bom_al_desc = db.Column(db.String)
    user_id = db.Column(db.Integer)
    orga_id = db.Column(db.Integer)
    kons_id = db.Column(db.Integer)
    mara_id = db.Column(db.Integer)
    fav = db.Column(db.Boolean)
    ext_mara_id = db.Column(db.String)
    ext_mara_desc = db.Column(db.String)
    cad_nr = db.Column(db.Integer)
    created_at = datetime
    updated_at = datetime
    auth_read = db.Column(db.Boolean)
    auth_write = db.Column(db.Boolean)
    auth_delete = db.Column(db.Boolean)
    auth_orga = db.Column(db.Boolean)
    del_kz = db.Column(db.Boolean)


    def __init__(self, bom_nr, bom_al, bom_al_desc,user_id, orga_id, kons_id, mara_id, fav, ext_mara_id, ext_mara_desc, cad_nr, created_at, updated_at, auth_read, auth_write, auth_delete, auth_orga, del_kz):
        self.bom_nr = bom_nr
        self.bom_al = bom_al
        self.bom_al_desc = bom_al_desc
        self.user_id = user_id
        self.orga_id = orga_id
        self.kons_id = kons_id
        self.mara_id = mara_id
        self.fav = fav
        self.ext_mara_id = ext_mara_id
        self.ext_mara_desc = ext_mara_desc
        self.cad_nr = cad_nr
        self.created_at = created_at
        self.updated_at = updated_at
        self.auth_read = auth_read
        self.auth_write = auth_write
        self.auth_delete = auth_delete
        self.auth_orga = auth_orga
        self.del_kz = del_kz

    ### GET, POST; PUT; DELETE
    def json(self):
        return { 'id' : self.id, 'bom_nr' : self.bom_nr, 'bom_al' : self.bom_al, 'bom_al_desc' : self.bom_al_desc, 'mara_id' : self.mara_id, 'fav' : self.fav, 'cad_nr' : self.cad_nr, 'del_kz' : self.del_kz}

    @classmethod
    def find_by_kons_id(cls, kons_id):
        sql = text("SELECT mast.id, mast.bom_nr, mast.bom_al, mast.bom_al_desc, mast.mara_id, mara.mara_nr, mara.mat_desc, mast.fav, mast.cad_nr, mast.del_kz FROM mast LEFT JOIN mara ON mast.mara_id=mara.id WHERE mast.kons_id=:kons_id")
        result = db.session.execute(sql, params={"kons_id": kons_id})
        return result.fetchall()


    #### POST PUT

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()