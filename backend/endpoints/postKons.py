from flask import Blueprint, request
from dbfunctions.connect import *
import json
import pandas as pd

postKons_bp = Blueprint('postKons', __name__)

@postKons_bp.route('/postKons', methods=["POST"])
def postKons():
    # Bekommt per POST Protokoll, Server, Port, Benutzername, Passwort, Datenbanktyp
    # Speichert das in lokaler sqlite datenbank als dict ab

    # {'IPPort': '4124', 'IPAddress': '12', 'protocol': 'fsdgfd', 'username': 'dfhg', 'password': 'dfgh'}
    # print(request.json)

    conn = connect_db()

    df = pd.read_sql_query("insert into kons values ('7', 'kons_title_test', 'kons_desc_test', '1', '1', '2020-06-16', 'NULL', '0')",conn)


    # Bei erfolg http status 200 zurückgeben an frontend
    #ret = {"id_database_severs": database_server["id_database_severs"]}
    print(df.head())
    return df.to_json(orient='records'), 200, {'ContentType': 'application/json'}
