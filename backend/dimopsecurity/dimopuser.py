# from dbfunctions.connect import *
# from flask import Blueprint, request
# from dbfunctions.connect import *
# import json
# import pandas as pd
# from flask_restful import Resource, reqparse

# getAllUser_bp = Blueprint('getAllUser', __name__)

#  class DimopUser():

#     def __init__(self, _id, firstname, e_mail):
#         self._id = _id
#         self.firstename = firstname
#         self.e_mail = e_mail
#         self.password = password



 

  #@classmethod
    #def find_by_email(cls, e_mail):
        #Datenbankverbindung
        #connection = sqlite3.connect ('data.db')
     #   conn = connect_db()

      #  query_e_mail = ("SELECT user.e_mail" FROM user, conn)
        #df = pd.read_sql_query("SELECT user.id, user.firstname, user.surname, user.e_mail, orga.orga_name, t_function.function, user.del_kz FROM user LEFT JOIN orga ON user.orga_id=orga.id LEFT JOIN t_function ON user.t_function_id=t_function.id", conn)

        #result = cursor.execute(query, (username,))
       # row = result. fetchone()
        #    if row not None:
         #       user = cls(*row) #_id, firstname, e_mail, password (row[0], row[1], row[2], row[3])
          #  else:
           #     user = None
            
           # return e_mail
#@getAllUser_bp.route('/getAllUser', methods=["GET"])
#def getAllUser():
    # Bekommt per POST Protokoll, Server, Port, Benutzername, Passwort, Datenbanktyp
    # Speichert das in lokaler sqlite datenbank als dict ab

    # {'IPPort': '4124', 'IPAddress': '12', 'protocol': 'fsdgfd', 'username': 'dfhg', 'password': 'dfgh'}
    # print(request.json)

 #   conn = connect_db()

  #  df = pd.read_sql_query("SELECT user.id, user.firstname, user.surname, user.e_mail, orga.orga_name, t_function.function, user.del_kz FROM user LEFT JOIN orga ON user.orga_id=orga.id LEFT JOIN t_function ON user.t_function_id=t_function.id", conn)

    # Bei erfolg http status 200 zurückgeben an frontend
    #ret = {"id_database_severs": database_server["id_database_severs"]}
    
    
    #print(df.head())
    #return df.to_json(orient='records'), 200, {'ContentType': 'application/json'}

#     @classmethod
#     def find_by_id(cls, _id):
#         #Datenbankverbindung
#         #connection = sqlite3.connect ('data.db')
#         conn = connect_db()

#         query_e_mail = ("SELECT user._id" FROM user, conn)
#         #df = pd.read_sql_query("SELECT user.id, user.firstname, user.surname, user.e_mail, orga.orga_name, t_function.function, user.del_kz FROM user LEFT JOIN orga ON user.orga_id=orga.id LEFT JOIN t_function ON user.t_function_id=t_function.id", conn)

#         #result = cursor.execute(query, (username,))
#         row = result. fetchone()
#             if row not None:
#                 user = cls(*row) #_id, firstname, e_mail, password (row[0], row[1], row[2], row[3])
#             else:
#                 user = None
            
#             return _id #user?

# class UserRegister(Resource):


#     parser = reqparse.RequestParser()
#     parser.add_argument('e_email',
#         type=str
#         required=True,
#         help="This field cannot be blank"
#     )
#     parser.add_argument('password',
#         type=str
#         required=True,
#         help="This field cannot be blank"
#     )
    
# ‚
#     def post(self):
#         data = UserRegister.parser.parse_args()
#         #check duplicates
#         #if DimopUser.find_by_email(data['e_mail']):
#          #   return {"message": "A user with that username already exists"}, 400


#         # Datenbank Verbindung
#         conn = connect_db()
#         query = "INSERT INTO user VALUES(NULL, ?, ?)" #Null = Autoinkrement
#                 #df = pd.read_sql_query("SELECT user.id, user.firstname, user.surname, user.e_mail, orga.orga_name, t_function.function, user.del_kz FROM user LEFT JOIN orga ON user.orga_id=orga.id LEFT JOIN t_function ON user.t_function_id=t_function.id", conn)

#         #cursor.execute(query,(data['username'], data[password']))
#         #commit save to disk
#         #close

#         return {"message": "User created successfully."}, 201

#         pass

# "id": "int",
 # "firstname": "string",
 # "surname": "string", 
 # "e_mail": "string", #obligatorisch  UI bitte Email einfügen
 # "orga_name ": "string",
 # "function": "string",
 # "del_kz": "boolean",
#}  