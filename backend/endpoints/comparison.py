"""
author: topr
last updated: 30.04.2021
currently used: yes
description: used to calculate recycling value
"""

from flask_restful import Resource, request
import pandas as pd
import numpy as np
import json
from dbfunctions.connect import connect_db
from topsis import topsis


class Comparison(Resource):

    def post(self):
        json_data = request.get_json(force=True)

        db_connection = connect_db()

        mat = pd.read_sql_query('SELECT * FROM mat', db_connection)

        result_data = mat.loc[mat["id"].isin(json_data["selectedIds"])][[
            "mat_rw", "price", "co2_value", "resource_use"]]

        alternatives = np.array(result_data)

        weights = np.array([float(json_data["recyclingWeight"]), float(json_data["priceWeight"]),
                            float(json_data["co2Weight"]), float(json_data["adpfWeight"])])

        directions = [1, 0, 0, 0]  # 0 = minimize, 1 = maximize

        result = topsis(alternatives, weights, directions)
        result.calc()
        scores = np.round(np.array(result.C), 3)
        ranks = np.array(
            [sorted(scores, reverse=True).index(x)+1 for x in scores])

        result_data["id"] = json_data["selectedIds"]
        result_data["mat_desc"] = mat.loc[mat["id"].isin(
            json_data["selectedIds"])]["mat_desc"]
        result_data["recycling_cat"] = mat.loc[mat["id"].isin(
            json_data["selectedIds"])]["recycling_cat"]
        result_data["score"] = scores
        result_data["ranks"] = ranks

        print(result_data)

        result_json = result_data.to_dict(orient="records")

        return result_json
