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
from itertools import product


class Comparison(Resource):

    def post(self):
        json_data = request.get_json(force=True)

        selected_ids = json_data["selectedIds"]
        recycling_weight = json_data["recyclingWeight"]
        price_weight = json_data["priceWeight"]
        co2_weight = json_data["co2Weight"]
        adpf_weight = json_data["adpfWeight"]

        print(selected_ids)
        print(recycling_weight)
        print(price_weight)
        print(co2_weight)
        print(adpf_weight)

        return 1
