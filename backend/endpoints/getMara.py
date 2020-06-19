from flask import Blueprint, request
from dbfunctions.connect import *
import json
import pandas as pd

getMara_bp = Blueprint('getMara', __name__)

@getMara_bp.route('/getMara', methods=["GET"])
def getMara():
    # Bekommt per POST Protokoll, Server, Port, Benutzername, Passwort, Datenbanktyp
    # Speichert das in lokaler sqlite datenbank als dict ab

    # {'IPPort': '4124', 'IPAddress': '12', 'protocol': 'fsdgfd', 'username': 'dfhg', 'password': 'dfgh'}
    # print(request.json)

    conn = connect_db()

    userid = request.args.get('userid')
    print(request.args.get('userid'))

    df = pd.read_sql_query("SELECT id, mara_nr, mat_desc, mat_int_desc, mat_rw, t_fam_id, campus_fam, user_id, t_mara_art_id, upload_kind, created_at, updated_at, dichte, unit, del_kz, producer FROM mara WHERE user_id='"+ userid + "'", conn)


    # Bei erfolg http status 200 zurückgeben an frontend
    #ret = {"id_database_severs": database_server["id_database_severs"]}
    print(df.head())
    return df.to_json(orient='records'), 200, {'ContentType': 'application/json'}
