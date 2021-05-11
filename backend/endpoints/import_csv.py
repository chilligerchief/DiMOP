"""
author: topr
last updated: 11.05.2021
currently used: yes
description: used to import data
"""

from flask_restful import Resource, request
from dbfunctions.connect import connect_db
from sqlalchemy import create_engine, MetaData, text
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from Models.mat import MatModel
from Models.bom import BomModel
from Models.rel import RelModel

# ToDos:
# - Check columns when upload
# - Check relations when upload
# - Check plastics when upload


class Import(Resource):

    def post(self):
        db = connect_db()

        json_data = request.get_json(force=True)
        bom = pd.DataFrame.from_dict(json_data["data"])
        rel = pd.DataFrame.from_dict(json_data["dataRelations"])
        orga_id = json_data["orgaId"]
        cons_id = json_data["selectedConstructionId"]

        print(f"orga_id: {orga_id}")
        print(f"cons_id: {cons_id}")
        print(f"rel:")
        print(rel)

        bom["mat_id"] = None

        # Iterate through bom an create new material entry for each row
        for i in range(0, bom.shape[0]):

            if(len(str(bom["mat_desc"][i])) > 0):
                mat_desc = bom["mat_desc"][i]
            else:
                mat_desc = None

            if(len(str(bom["mat_id_int"][i])) > 0):
                mat_id_int = bom["mat_id_int"][i]
            else:
                mat_id_int = None

            if(len(str(bom["mat_desc_int"][i])) > 0):
                mat_desc_int = bom["mat_desc_int"][i]
            else:
                mat_desc_int = None

            if(len(str(bom["cad_id"][i])) > 0):
                cad_id = bom["cad_id"][i]
            else:
                cad_id = None

            if(len(str(bom["height"][i])) > 0):
                height = bom["height"][i]
            else:
                height = None

            if(len(str(bom["width"][i])) > 0):
                width = bom["width"][i]
            else:
                width = None

            if(len(str(bom["depth"][i])) > 0):
                depth = bom["depth"][i]
            else:
                depth = None

            if(len(str(bom["weight"][i])) > 0):
                weight = bom["weight"][i]
            else:
                weight = None

            if(len(str(bom["volume"][i])) > 0):
                volume = bom["volume"][i]
            else:
                volume = None

            if(len(str(bom["is_atomic"][i])) > 0):
                is_atomic = bom["is_atomic"][i]
            else:
                is_atomic = None

            if(len(str(bom["plast_desc"][i])) > 0):
                plast = pd.read_sql_query(
                    f'SELECT * FROM plast WHERE mat_desc="{bom["plast_desc"][i]}"', db)
                print("plast")
                print(plast)
                mara_plast_id = None
            else:
                mara_plast_id = None

            new_mat_entry = MatModel(mat_desc=mat_desc, mat_id_int=mat_id_int, mat_desc_int=mat_desc_int, cad_id=cad_id, mara_plast_id=mara_plast_id, mat_rw=None, height=height, width=width, depth=depth, unit="mm", weight=weight, weight_unit="g",
                                     volume=volume, volume_unit="mm^3", is_atomic=is_atomic, orga_id=orga_id, cons_id=cons_id, del_kz=0, price=None, co2_value=None, resource_use=None, recycling_cat=None, evaluated=None, impure=None, dangerous=None)

            new_mat_entry.save_to_db()

            mat = pd.read_sql_query('SELECT * FROM mat', db)
            newest_mat = mat["id"].tolist()[mat.shape[0]-1]
            bom["mat_id"][i] = newest_mat

        # Iterate through bom an create new bom entry for each row
        for i in range(1, bom.shape[0]):

            mat_id = bom["mat_id"][i]

            parent_mat_id = bom.loc[bom["id"] == str(
                int(float(bom["parent_id"][i])))]["mat_id"].tolist()[0]

            print(f"parent_mat_id: {parent_mat_id}")

            new_bom_entry = BomModel(
                mat_id=mat_id, parent_mat_id=parent_mat_id)

            new_bom_entry.save_to_db()

        # Iterate though relations an create new rel entry for each row
        for i in range(0, rel.shape[0]):

            new_rel_entry = RelModel(
                p_id=rel["p_id"][i], m1_id=rel["m1_id"][i], m2_id=rel["m2_id"][i], rel_type=rel["rel_type"][i])

            new_rel_entry.save_to_db()

        return "Everything worked just fine!"
