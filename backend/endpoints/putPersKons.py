from flask import Blueprint, request
from dbfunctions.connect import *
import json
import pandas as pd

putPersKons_bp = Blueprint('putPersKons', __name__)

@putPersKons_bp.route('/putPersKons', methods=["PUT"])
def putPersKons():
    # Bekommt per POST Protokoll, Server, Port, Benutzername, Passwort, Datenbanktyp
    # Speichert das in lokaler sqlite datenbank als dict ab

    # {'IPPort': '4124', 'IPAddress': '12', 'protocol': 'fsdgfd', 'username': 'dfhg', 'password': 'dfgh'}
    # print(request.json)

    conn = connect_db()

    konsid = request.args.get('konsid')
    print(request.args.get('konsid'))

    df = pd.read_sql_query("PUT user.*, orga.orga_name FROM perp LEFT JOIN user ON (user.id=perp.user_id) left join orga ON (user.orga_id=orga.id) WHERE kons_id='"+ konsid + "'", conn)


    # Bei erfolg http status 200 zurückgeben an frontend
    #ret = {"id_database_severs": database_server["id_database_severs"]}
    print(df.head())
    return df.to_json(orient='records'), 200, {'ContentType': 'application/json'}
