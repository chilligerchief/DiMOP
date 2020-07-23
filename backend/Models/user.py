from dbfunctions.connect import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    e_mail = db.Column(db.String(255))
    orga_id = db.Column(db.Integer) #db.ForeignKey('orga_id.id')
    t_function_id = db.Column(db.Integer) #db.ForeignKey('t_function.id')
    created_at = datetime
    updated_at = datetime
    password = db.Column(db.String(1024))
    pw_salt = db.Column(db.String(1024))
    ver_indicator = db.Column(db.Boolean)
    del_kz = db.Column(db.Boolean)


    def __init__(self, firstname, surname, t_function_id, e_mail, password, orga_id=None, created_at=None, updated_at=None, pw_salt=None, ver_indicator=None, del_kz=None):
        self.firstname = firstname
        self.surname = surname
        self.e_mail = e_mail
        self.orga_id = orga_id
        self.t_function_id = t_function_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.password = password
        self.pw_salt = pw_salt
        self.ver_indicator = ver_indicator
        self.del_kz = del_kz

    ### GET, POST; PUT; DELETE
    def json(self):
        return { 'id' : self.id, 'firstname' : self.firstname, 'surname' : self.surname, 'e_mail' : self.e_mail, 'orga_id' : self.orga_id, 't_function_id' : self.t_function_id, 'del_kz' : self.del_kz}


    @classmethod
    def find_by_surname(cls, surname):
        return cls.query.filter_by(surname=surname).first()

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
# # conn = connect_db()

# #     df = pd.read_sql_query("SELECT user.id, user.firstname, user.surname, user.e_mail, orga.orga_name, t_function.function, user.del_kz FROM user LEFT JOIN orga ON user.orga_id=orga.id LEFT JOIN t_function ON user.t_function_id=t_function.id", conn)

# #     # Bei erfolg http status 200 zurückgeben an frontend
# #     #ret = {"id_database_severs": database_server["id_database_severs"]}
# #     print(df.head())
# #     return df.to_json(orient='records'), 200, {'ContentType': 'application/json'}
