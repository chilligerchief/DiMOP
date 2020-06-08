from flask import Blueprint, request
from dbfunctions.connect import *
import json
import pandas as pd

getUser_bp = Blueprint('getUser', __name__)

@getUser_bp.route('/getUser', methods=["GET"])
def getUser():
    # Bekommt per POST Protokoll, Server, Port, Benutzername, Passwort, Datenbanktyp
    # Speichert das in lokaler sqlite datenbank als dict ab

    # {'IPPort': '4124', 'IPAddress': '12', 'protocol': 'fsdgfd', 'username': 'dfhg', 'password': 'dfgh'}
    # print(request.json)

    df = pd.read_sql_query("SELECT user.id, user.firstname, user.surname, user.e_mail, orga.orga_name, t_function.function FROM user LEFT join orga ON (orga.id=user.orga_id) LEFT join t_function ON (t_function.id=user.t_function_id)")


    # Bei erfolg http status 200 zurückgeben an frontend
    #ret = {"id_database_severs": database_server["id_database_severs"]}
    print(df.head())
    return df.to_json(orient='records'), 200, {'ContentType': 'application/json'}