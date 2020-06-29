from flask import Blueprint, request
from dbfunctions.connect_test import *
import json
import pandas as pd

getKons_bp = Blueprint('getKons', __name__)

@getKons_bp.route('/getKons', methods=["GET"])
def getKons():
    # Bekommt per POST Protokoll, Server, Port, Benutzername, Passwort, Datenbanktyp
    # Speichert das in lokaler sqlite datenbank als dict ab

    # {'IPPort': '4124', 'IPAddress': '12', 'protocol': 'fsdgfd', 'username': 'dfhg', 'password': 'dfgh'}
    # print(request.json)

    conn = db

    userid = request.args.get('userid')
    print(request.args.get('userid'))

    df = cursor.execute("SELECT kons.* FROM perp LEFT JOIN kons ON perp.kons_id=kons.id WHERE user_id='"+ userid + "'", conn)


    # Bei erfolg http status 200 zurückgeben an frontend
    #ret = {"id_database_severs": database_server["id_database_severs"]}
    print(df.head())
    return df.to_json(orient='records'), 200, {'ContentType': 'application/json'}
