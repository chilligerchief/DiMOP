from flask_restful import Resource, reqparse
from Models.function import FunctionModel


class Function(Resource):
    def get(self):
        return {'Funktionen': [x.json() for x in FunctionModel.query.all()]}


        #db = mysql.connect(host="132.187.102.201", user="milena", passwd="ALAQsM8W", database='dimop')
        #cursor = db.cursor()
        #query = 'Select * from t_function'
        #output = cursor.execute(query)
        #return json.dumps(output)
        #output = db.engine.execute(query)
        #return json.dumps(output)

        #t_function = FunctionModel.query.all()
        #return t_function.json() #FunctionModel.json(t_function)