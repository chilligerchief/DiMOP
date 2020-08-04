from dbfunctions.connect import db

class BomItemModel(db.Model):
    __tablename__ = 'stpo'

    id = db.Column(db.Integer, primary_key=True)
    mast_id = db.Column(db.Integer)
    mara_id = db.Column(db.Integer)
    pos = db.Column(db.Integer)
    height_erp = db.Column(db.Float)
    width_erp = db.Column(db.Float)
    depth_erp = db.Column(db.Float)
    unit_erp = db.Column(db.String)
    volume_cad = db.Column(db.Float)
    unit_cad = db.Column(db.String)
    weight_ui = db.Column(db.String)
    qr_relevant = db.Column(db.Boolean)

    def __init__(self, mast_id, mara_id, pos, height_erp, width_erp, depth_erp, unit_erp, volume_cad, unit_cad, weight_ui, qr_relevant):
        self.mast_id = mast_id
        self.mara_id = mara_id
        self.pos = pos
        self.height_erp = height_erp
        self.width_erp = width_erp
        self.depth_erp = depth_erp
        self.unit_erp = unit_erp
        self.volume_cad = volume_cad
        self.unit_cad = unit_cad
        self.weight_ui = weight_ui
        self.qr_relevant = qr_relevant

    ### GET, POST; PUT; DELETE
    def json(self):
        return { 'id' : self.id, 'mast_id' : self.mast_id, 'mara_id' : self.mara_id, 'pos' : self.pos, 'height_erp' : self.height_erp, 'width_erp' : self.width_erp, 'depth_erp' : self.depth_erp, 'volume_cad' : self.volume_cad, 'unit_cad' : self.unit_cad, 'weight_ui' : self.weight_ui, 'qr_relevant' : self.qr_relevant}

    @classmethod
    def find_by_mast_id(cls, mast_id):
        return cls.query.filter_by(mast_id=mast_id)


    #### POST PUT

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()