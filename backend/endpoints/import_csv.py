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


class Import(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        bom = pd.DataFrame.from_dict(json_data["data"])
        orga_id = json_data["orgaId"]
        cons_id = json_data["selectedConstructionId"]
        bom["mat_id"] = None

        # for i in range(0, bom.shape[0]):
        for i in range(0, 1):

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

            mat = MatModel(mat_desc=mat_desc, mat_id_int=mat_id_int, mat_desc_int=mat_desc_int, cad_id=cad_id, mara_plast_id=None, mat_rw=None, height=height, width=width, depth=depth, unit="mm", weight=weight, weight_unit="g",
                           volume=volume, volume_unit="mm^3", is_atomic=is_atomic, orga_id=orga_id, cons_id=cons_id, del_kz=0, price=None, co2_value=None, resource_use=None, recycling_cat=None, evaluated=None, impure=None, dangerous=None)

            print(mat)

            # mat.save_to_db()

        return "Everything worked just fine!"
