from dbfunctions.connect import db
from datetime import datetime

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
    dichte = db.Column(db.String)
    unit = db.Column(db.String)
    del_kz = db.Column(db.Boolean)
    producer = db.Column(db.String)
    Verarbeitungsmethode = db.Column(db.String)
    Belastung = db.Column(db.String)
    Temperatur = db.Column(db.String)
    MVR = db.Column(db.String)
    Bruchdehnung = db.Column(db.String)
    Bruchdehnung_Nominell = db.Column(db.String)
    Bruchdehnung_TPE = db.Column(db.String)
    Bruchdehnung_Senkrecht = db.Column(db.String)
    Bruchdehnung_Parallel = db.Column(db.String)
    Bruchspannung_MPa = db.Column(db.String)
    Bruchspannung_TPE_MPa = db.Column(db.String)
    Bruchspannung_Parallel_MPa = db.Column(db.String)
    Bruchspannung_Senkrecht_Mpa = db.Column(db.String)
    Zugmodul_MPa = db.Column(db.String)
    Zugmodul_Kriech_1h_MPa = db.Column(db.String)
    Zugmodul_Kriech_1000h_MPa = db.Column(db.String)
    Zugmodul_Parallel_MPa = db.Column(db.String)
    Zugmodul_Senkrecht_MPa = db.Column(db.String)


    def __init__(self, mara_nr, mat_desc, mat_int_desc,mat_rw, t_fam_id, campus_fam, user_id, t_mara_art_id, upload_kind, created_at, updated_at, dichte, unit,del_kz,producer,Verarbeitungsmethode, Belastung, Temperatur, MVR, Bruchdehnung, Bruchdehnung_Nominell, Bruchdehnung_TPE, Bruchdehnung_Senkrecht, Bruchdehnung_Parallel, Bruchspannung_MPa, Bruchspannung_TPE_MPa, Bruchspannung_Parallel_MPa, Bruchspannung_Senkrecht_Mpa, Zugmodul_MPa, Zugmodul_Kriech_1h_MPa, Zugmodul_Kriech_1000h_MPa, Zugmodul_Parallel_MPa, Zugmodul_Senkrecht_MPa):
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
        self.dichte = dichte
        self.unit = unit
        self.del_kz = del_kz
        self.producer = producer
        self.Verarbeitungsmethode = Verarbeitungsmethode
        self.Belastung = Belastung
        self.Temperatur = Temperatur
        self.MVR = MVR
        self.Bruchdehnung = Bruchdehnung
        self.Bruchdehnung_Nominell = Bruchdehnung_Nominell
        self.Bruchdehnung_TPE = Bruchdehnung_TPE
        self.Bruchdehnung_Senkrecht = Bruchdehnung_Senkrecht
        self.Bruchdehnung_Parallel = Bruchdehnung_Parallel
        self.Bruchspannung_MPa = Bruchspannung_MPa
        self.Bruchspannung_TPE_MPa = Bruchspannung_TPE_MPa
        self.Bruchspannung_Parallel_MPa = Bruchspannung_Parallel_MPa
        self.Bruchspannung_Senkrecht_Mpa = Bruchspannung_Senkrecht_Mpa
        self.Zugmodul_MPa = Zugmodul_MPa
        self.Zugmodul_Kriech_1h_MPa = Zugmodul_Kriech_1h_MPa
        self.Zugmodul_Kriech_1000h_MPa = Zugmodul_Kriech_1000h_MPa
        self.Zugmodul_Parallel_MPa = Zugmodul_Parallel_MPa
        self.Zugmodul_Senkrecht_MPa = Zugmodul_Senkrecht_MPa

    ### GET, POST; PUT; DELETE
    def json(self):
        return { 'mara_nr' : self.mara_nr, 'mat_desc' : self.mat_desc, 'mat_int_desc' : self.mat_int_desc, 'mat_rw' : self.mat_rw, 't_fam_id' : self.t_fam_id, 'campus_fam' : self.campus_fam, 'user_id' : self.user_id,
                 't_mara_art_id' : self.t_mara_art_id, 'upload_kind' : self.upload_kind, 'created_at' : self.created_at, 'updated_at' : self.updated_at, 'dichte' : self.dichte, 'unit' : self.unit, 'del_kz' : self.del_kz,
                 'producer' : self.producer, 'Verarbeitungsmethode' : self.Verarbeitungsmethode, 'Belastung' : self.Belastung, 'Temperatur' : self.Temperatur, 'MVR' : self.MVR, 'Bruchdehnung' : self.Bruchdehnung,
                 'Bruchdehnung_Nominell' : self.Bruchdehnung_Nominell, 'Bruchdehnung_TPE' : self.Bruchdehnung_TPE, 'Bruchdehnung_Senkrecht' : self.Bruchdehnung_Senkrecht, 'Bruchdehnung_Parallel' : self.Bruchdehnung_Parallel,
                 'Bruchspannung_MPa' : self.Bruchspannung_MPa, 'Bruchspannung_TPE_MPa' : self.Bruchspannung_TPE_MPa, 'Bruchspannung_Parallel_MPa' : self.Bruchspannung_Parallel_MPa, 'Bruchspannung_Senkrecht_Mpa' : self.Bruchspannung_Senkrecht_Mpa,
                 'Zugmodul_MPa' : self.Zugmodul_MPa, 'Zugmodul_Kriech_1h_MPa' : self.Zugmodul_Kriech_1h_MPa, 'Zugmodul_Kriech_1000h_MPa' : self.Zugmodul_Kriech_1000h_MPa, 'Zugmodul_Parallel_MPa' : self.Zugmodul_Parallel_MPa, 'Zugmodul_Senkrecht_MPa' : self.Zugmodul_Senkrecht_MPa}

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id)

    #### POST PUT

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()