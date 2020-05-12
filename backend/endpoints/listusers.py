from flask import Blueprint, request
import * from dbfunctions.connect
import json
import pandas as pd


@setServer_bp.route('/getUsers', methods=["GET"])
def setServer():
    # Bekommt per POST Protokoll, Server, Port, Benutzername, Passwort, Datenbanktyp
    # Speichert das in lokaler sqlite datenbank als dict ab

    # {'IPPort': '4124', 'IPAddress': '12', 'protocol': 'fsdgfd', 'username': 'dfhg', 'password': 'dfgh'}
    # print(request.json)

    conn = connect_db()

    konsid = request.form.get('konsid')
    print(request.form.get('konsid'))

    df = pd.read_sql_query("SELECT * FROM perp LEFT JOIN user ON (perp.user_id = user.id) WHERE kons_id='"+ konsid + "'", conn)


    # Bei erfolg http status 200 zurückgeben an frontend
    #ret = {"id_database_severs": database_server["id_database_severs"]}

    return df.to_json(), 200, {'ContentType': 'application/json'}
