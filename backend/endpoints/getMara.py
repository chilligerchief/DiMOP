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

    df = pd.read_sql_query("SELECT mara.id, mara.mara_nr, mara.mat_desc, mara.mat_int_desc, mara.mat_rw, t_fam.fam_dimop_desc, mara.campus_fam, user.firstname, user.surname, t_mara_art.art, mara.upload_kind, mara.created_at, mara.updated_at, mara.dichte, mara.unit, mara.del_kz, mara.producer FROM mara LEFT JOIN t_fam ON mara.t_fam_id=t_fam.id LEFT JOIN t_mara_art ON mara.t_mara_art_id=t_mara_art.id LEFT JOIN user ON mara.user_id=user.id WHERE mara.user_id='"+ userid + "'", conn)


    # Bei erfolg http status 200 zurückgeben an frontend
    #ret = {"id_database_severs": database_server["id_database_severs"]}
    print(df.head())
    return df.to_json(orient='records'), 200, {'ContentType': 'application/json'}
