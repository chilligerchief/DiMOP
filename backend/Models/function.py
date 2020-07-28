from dbfunctions.connect import db

class FunctionModel(db.Model):
    __tablename__ = 't_function'

    id = db.Column(db.Integer, primary_key=True)
    function = db.Column(db.String(255))

    def __init__(self, function):
        self.function = function

    def json(self):
        return {'id' : self.id, 'function': self.function}

    @classmethod
    def get_all(cls):
        return cls.query.all()