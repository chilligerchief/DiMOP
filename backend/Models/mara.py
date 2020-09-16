from dbfunctions.connect import db
from datetime import datetime
from sqlalchemy import text

class MaraModel(db.Model):
    __tablename__ = 'mara'

    id = db.Column(db.Integer, primary_key=True)
    mara_nr = db.Column(db.String)
    mat_desc = db.Column(db.String)
    mat_int_desc = db.Column(db.String)
    mat_rw = db.Column(db.Float)
    t_fam_id = db.Column(db.Integer)
    campus_fam = db.Column(db.String)
    user_id = db.Column(db.Integer)
    t_mara_art_id = db.Column(db.Integer)
    upload_kind = db.Column(db.String)
    created_at = datetime
    updated_at = datetime

    dichte_trocken = db.Column(db.Float)
    dichte_konditioniert = db.Column(db.Float)

    unit = db.Column(db.String)
    del_kz = db.Column(db.Boolean)
    producer = db.Column(db.String)
    Verarbeitungsmethode = db.Column(db.String)

    Belastung_trocken = db.Column(db.Float)
    Belastung_konditioniert = db.Column(db.Float)

    Temperatur_trocken_trocken = db.Column(db.Float)
    Temperatur_trocken_konditioniert = db.Column(db.Float)

    MVR_trocken_trocken = db.Column(db.Float)
    MVR_trocken_konditioniert = db.Column(db.Float)

    Bruchdehnung_trocken = db.Column(db.Float)
    Bruchdehnung_konditioniert = db.Column(db.Float)

    Bruchdehnung_Nominell_trocken = db.Column(db.Float)
    Bruchdehnung_Nominell_konditioniert = db.Column(db.Float)

    Bruchdehnung_TPE_trocken = db.Column(db.Float)
    Bruchdehnung_TPE_konditioniert = db.Column(db.Float)

    Bruchdehnung_Parallel_trocken = db.Column(db.Float)
    Bruchdehnung_Parallel_konditioniert = db.Column(db.Float)

    Bruchspannung_MPa_trocken = db.Column(db.Float)
    Bruchspannung_MPa_konditioniert = db.Column(db.Float)

    Bruchspannung_TPE_MPa_trocken = db.Column(db.Float)
    Bruchspannung_TPE_MPa_konditioniert = db.Column(db.Float)

    Bruchspannung_Parallel_MPa_trocken = db.Column(db.Float)
    Bruchspannung_Parallel_MPa_konditioniert = db.Column(db.Float)

    Bruchspannung_Senkrecht_Mpa_trocken = db.Column(db.Float)
    Bruchspannung_Senkrecht_Mpa_konditioniert = db.Column(db.Float)

    Zugmodul_MPa_trocken = db.Column(db.Float)
    Zugmodul_MPa_konditioniert = db.Column(db.Float)

    Zugmodul_Kriech_1h_MPa_trocken = db.Column(db.Float)
    Zugmodul_Kriech_1h_MPa_konditioniert = db.Column(db.Float)

    Zugmodul_Kriech_1000h_MPa_trocken = db.Column(db.Float)
    Zugmodul_Kriech_1000h_MPa_konditioniert = db.Column(db.Float)

    Zugmodul_Parallel_MPa_trocken = db.Column(db.Float)
    Zugmodul_Parallel_MPa_konditioniert = db.Column(db.Float)

    Zugmodul_Senkrecht_MPa_trocken = db.Column(db.Float)
    Zugmodul_Senkrecht_MPa_konditioniert = db.Column(db.Float)

    def __init__(self, mara_nr, mat_desc, t_fam_id, dichte_trocken, dichte_konditioniert, mat_int_desc=None,mat_rw=None, campus_fam=None, user_id=None, t_mara_art_id=None, upload_kind=None, created_at=None, updated_at=None, unit=None,del_kz=None,producer=None,Verarbeitungsmethode=None, Belastung_trocken=None, Belastung_konditioniert=None, 
    Temperatur_trocken=None, Temperatur_konditioniert=None, MVR_trocken=None, MVR_konditioniert=None, Bruchdehnung_trocken=None, Bruchdehnung_konditioniert=None,
    Bruchdehnung_Nominell_trocken=None, Bruchdehnung_Nominell_konditioniert=None, 
    Bruchdehnung_TPE_trocken=None, Bruchdehnung_TPE_konditioniert=None, 
    Bruchdehnung_Parallel_trocken=None, Bruchdehnung_Parallel_konditioniert=None, 
    Bruchspannung_MPa_trocken=None, Bruchspannung_MPa_konditioniert=None, 
    Bruchspannung_TPE_MPa_trocken=None, Bruchspannung_TPE_MPa_konditioniert=None, 
    Bruchspannung_Parallel_MPa_trocken=None, Bruchspannung_Parallel_MPa_konditioniert=None, 
    Bruchspannung_Senkrecht_Mpa_trocken=None, Bruchspannung_Senkrecht_Mpa_konditioniert=None, 
    Zugmodul_MPa_trocken=None, Zugmodul_MPa_konditioniert=None, 
    Zugmodul_Kriech_1h_MPa_trocken=None, Zugmodul_Kriech_1h_MPa_konditioniert=None, 
    Zugmodul_Kriech_1000h_MPa_trocken=None, Zugmodul_Kriech_1000h_MPa_konditioniert=None, 
    Zugmodul_Parallel_MPa_trocken=None, Zugmodul_Parallel_MPa_konditioniert=None, 
    Zugmodul_Senkrecht_MPa_trocken=None, Zugmodul_Senkrecht_MPa_konditioniert=None):
        self.mara_nr = mara_nr
        self.mat_desc = mat_desc
        self.mat_int_desc = mat_int_desc
        self.mat_rw = mat_rw
        self.t_fam_id = t_fam_id
        self.campus_fam = campus_fam
        self.user_id = user_id
        self.t_mara_art_id = t_mara_art_id
        self.upload_kind = upload_kind
        self.created_at = created_at
        self.updated_at = updated_at
        self.dichte_trocken = dichte_trocken
        self.dichte_konditioniert = dichte_konditioniert
        self.unit = unit
        self.del_kz = del_kz
        self.producer = producer
        self.Verarbeitungsmethode = Verarbeitungsmethode
        self.Belastung_trocken = Belastung_trocken
        self.Belastung_konditioniert = Belastung_konditioniert
        self.Temperatur_trocken = Temperatur_trocken
        self.Temperatur_konditioniert = Temperatur_konditioniert
        self.MVR_trocken = MVR_trocken
        self.MVR_konditioniert = MVR_konditioniert
        self.Bruchdehnung_trocken = Bruchdehnung_trocken
        self.Bruchdehnung_konditioniert = Bruchdehnung_konditioniert
        self.Bruchdehnung_Nominell_trocken = Bruchdehnung_Nominell_trocken
        self.Bruchdehnung_Nominell_konditioniert = Bruchdehnung_Nominell_konditioniert
        self.Bruchdehnung_TPE_trocken = Bruchdehnung_TPE_trocken
        self.Bruchdehnung_TPE_konditioniert = Bruchdehnung_TPE_konditioniert
        self.Bruchdehnung_Parallel_trocken = Bruchdehnung_Parallel_trocken
        self.Bruchdehnung_Parallel_konditioniert = Bruchdehnung_Parallel_konditioniert

        self.Bruchspannung_MPa_trocken = Bruchspannung_MPa_trocken
self.Bruchspannung_MPa_konditioniert = Bruchspannung_MPa_konditioniert


        self.Bruchspannung_TPE_MPa_trocken  = Bruchspannung_TPE_MPa_trocken
self.Bruchspannung_TPE_MPa_konditioniert = Bruchspannung_TPE_MPa_konditioniert

        self.Bruchspannung_Parallel_MPa_trocken = Bruchspannung_Parallel_MPa_trocken
self.Bruchspannung_Parallel_MPa_konditioniert = Bruchspannung_Parallel_MPa_konditioniert

        self.Bruchspannung_Senkrecht_Mpa_trocken = Bruchspannung_Senkrecht_Mpa_trocken
self.Bruchspannung_Senkrecht_Mpa_konditioniert = Bruchspannung_Senkrecht_Mpa_konditioniert

        self.Zugmodul_MPa_trocken = Zugmodul_MPa_trocken
self.Zugmodul_MPa_konditioniert = Zugmodul_MPa_konditioniert

        self.Zugmodul_Kriech_1h_MPa_trocken = Zugmodul_Kriech_1h_MPa_trocken
self.Zugmodul_Kriech_1h_MPa_konditioniert = Zugmodul_Kriech_1h_MPa_konditioniert

        self.Zugmodul_Kriech_1000h_MPa_trocken = Zugmodul_Kriech_1000h_MPa_trocken
 self.Zugmodul_Kriech_1000h_MPa_konditioniert = Zugmodul_Kriech_1000h_MPa_konditioniert

        self.Zugmodul_Parallel_MPa_trocken = Zugmodul_Parallel_MPa_trocken
self.Zugmodul_Parallel_MPa_konditioniert = Zugmodul_Parallel_MPa_konditioniert

        self.Zugmodul_Senkrecht_MPa_trocken = Zugmodul_Senkrecht_MPa_trocken
self.Zugmodul_Senkrecht_MPa_konditioniert = Zugmodul_Senkrecht_MPa_konditioniert
    def json(self):
        return { 'id' : self.id, 'mara_nr' : self.mara_nr, 'mat_desc' : self.mat_desc, 'mat_int_desc' : self.mat_int_desc, 'mat_rw' : self.mat_rw, 't_fam_id' : self.t_fam_id, 'campus_fam' : self.campus_fam, 'user_id' : self.user_id,
                 't_mara_art_id' : self.t_mara_art_id, 'upload_kind' : self.upload_kind, 'dichte_trocken' : self.dichte_trocken, 'unit' : self.unit, 'del_kz' : self.del_kz,
                 'producer' : self.producer, 'Verarbeitungsmethode' : self.Verarbeitungsmethode, 'Belastung' : self.Belastung, 'Temperatur_trocken' : self.Temperatur_trocken, 'MVR_trocken' : self.MVR_trocken, 'Bruchdehnung' : self.Bruchdehnung,
                 'Bruchdehnung_Nominell' : self.Bruchdehnung_Nominell, 'Bruchdehnung_TPE' : self.Bruchdehnung_TPE, 'Bruchdehnung_Senkrecht' : self.Bruchdehnung_Senkrecht, 'Bruchdehnung_Parallel' : self.Bruchdehnung_Parallel,
                 'Bruchspannung_MPa' : self.Bruchspannung_MPa, 'Bruchspannung_TPE_MPa' : self.Bruchspannung_TPE_MPa, 'Bruchspannung_Parallel_MPa' : self.Bruchspannung_Parallel_MPa, 'Bruchspannung_Senkrecht_Mpa' : self.Bruchspannung_Senkrecht_Mpa,
                 'Zugmodul_MPa' : self.Zugmodul_MPa, 'Zugmodul_Kriech_1h_MPa' : self.Zugmodul_Kriech_1h_MPa, 'Zugmodul_Kriech_1000h_MPa' : self.Zugmodul_Kriech_1000h_MPa, 'Zugmodul_Parallel_MPa' : self.Zugmodul_Parallel_MPa, 'Zugmodul_Senkrecht_MPa' : self.Zugmodul_Senkrecht_MPa }


    @classmethod
    def find_by_user_id(cls, user_id):
        sql = text("SELECT mara.id, mara.mara_nr, mara.mat_desc, mara.mat_int_desc, mara.mat_rw, mara.t_fam_id, t_fam.fam_dimop_desc, mara.campus_fam, mara.user_id, user.firstname, user.surname, mara.t_mara_art_id, t_mara_art.art, mara.upload_kind, mara.dichte_trocken, mara.unit, mara.del_kz, mara.producer, mara.Verarbeitungsmethode, mara.Belastung, mara.Temperatur_trocken, mara.MVR_trocken, mara.Bruchdehnung, mara.Bruchdehnung_Nominell, mara.Bruchdehnung_TPE, mara.Bruchdehnung_Parallel, mara.Bruchdehnung_Senkrecht, mara.Bruchspannung_MPa, mara.Bruchspannung_TPE_MPa, mara.Bruchspannung_Parallel_MPa, mara.Bruchspannung_Senkrecht_MPa, mara.Zugmodul_MPa, mara.Zugmodul_Kriech_1h_MPa, mara.Zugmodul_Kriech_1000h_MPa, mara.Zugmodul_Parallel_MPa, mara.Zugmodul_Senkrecht_MPa FROM mara LEFT JOIN t_fam ON mara.t_fam_id=t_fam.id LEFT JOIN t_mara_art ON mara.t_mara_art_id=t_mara_art.id LEFT JOIN user ON mara.user_id=user.id WHERE mara.user_id=:user_id")
        result = db.session.execute(sql, params={"user_id": user_id})
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