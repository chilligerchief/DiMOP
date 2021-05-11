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


class Import(Resource):

    def post(self):

        json_data = request.get_json(force=True)
        bom = pd.DataFrame.from_dict(json_data["data"])
        rel = pd.DataFrame.from_dict(json_data["dataRelations"])
        orga_id = json_data["orgaId"]
        cons_id = json_data["selectedConstructionId"]

        if(1 == 0):

            #
            #
            # Hier kommt noch was hin :)
            #
            #
            #

            return 0

        else:
            db = connect_db()
            plast = pd.read_sql_query(f'SELECT * FROM plast', db)

            bom["mat_id"] = None

            # Iterate through bom an create new material entry for each row
            for i in range(0, bom.shape[0]):

                mat_desc = None
                mat_id_int = None
                mat_desc_int = None
                mara_plast_id = None
                cad_id = None
                height = None
                width = None
                depth = None
                weight = None
                volume = None
                is_atomic = None

                try:
                    if(len(str(bom["mat_desc"][i])) > 0):
                        mat_desc = bom["mat_desc"][i]
                except:
                    print(f"error: mat_desc")

                try:
                    if(len(str(bom["mat_id_int"][i])) > 0):
                        mat_id_int = bom["mat_id_int"][i]
                except:
                    print(f"error: mat_id_int")

                try:
                    if(len(str(bom["mat_desc_int"][i])) > 0):
                        mat_desc_int = bom["mat_desc_int"][i]
                except:
                    print(f"error: mat_desc_int")

                try:
                    if(len(str(bom["cad_id"][i])) > 0):
                        cad_id = bom["cad_id"][i]
                except:
                    print(f"error: cad_id")

                try:
                    if(len(str(bom["height"][i])) > 0):
                        height = bom["height"][i]
                except:
                    print(f"error: height")

                try:
                    if(len(str(bom["width"][i])) > 0):
                        width = bom["width"][i]
                except:
                    print(f"error: width")

                try:
                    if(len(str(bom["depth"][i])) > 0):
                        depth = bom["depth"][i]
                except:
                    print(f"error: depth")

                try:
                    if(len(str(bom["weight"][i])) > 0):
                        weight = bom["weight"][i]
                except:
                    print(f"error: weight")

                try:
                    if(len(str(bom["volume"][i])) > 0):
                        volume = bom["volume"][i]
                except:
                    print(f"error: volume")

                try:
                    if(len(str(bom["is_atomic"][i])) > 0):
                        is_atomic = bom["is_atomic"][i]
                except:
                    print(f"error: is_atomic")

                try:
                    description = bom["plast_desc"][i]
                    family = bom["plast_fam"][i]
                    plast_descriptions = plast.loc[plast["del_kz"] == 1.0]["mat_desc"].tolist(
                    )
                    plast_families = list(
                        set(plast.loc[plast["del_kz"] == 1.0]["campus_fam"].tolist()))

                    if(description in plast_descriptions):
                        mara_plast_id = plast.loc[plast["mat_desc"] == description]["id"].tolist()[
                            0]
                    elif(family in plast_families):
                        mara_plast_id = plast.loc[plast["mat_desc"] == f"Dummy_{family}"]["id"].tolist()[
                            0]
                except:
                    print(f"error: mara_plast_id")

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

                new_bom_entry = BomModel(
                    mat_id=mat_id, parent_mat_id=parent_mat_id)

                new_bom_entry.save_to_db()

            # Iterate though relations an create new rel entry for each row
            for i in range(0, rel.shape[0]):

                p_id = bom.loc[bom["id"] == str(
                    rel["p_id"][i])]["mat_id"].tolist()[0]
                m1_id = bom.loc[bom["id"] == str(
                    rel["m1_id"][i])]["mat_id"].tolist()[0]
                m2_id = bom.loc[bom["id"] == str(
                    rel["m2_id"][i])]["mat_id"].tolist()[0]
                rel_type = rel["rel_type"][i]

                new_rel_entry = RelModel(
                    p_id=p_id, m1_id=m1_id, m2_id=m2_id, rel_type=rel_type)

                new_rel_entry.save_to_db()

            return 1
