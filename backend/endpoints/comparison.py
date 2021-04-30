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

        print(json_data["selectedIds"])
        print(json_data["recyclingWeight"])
        print(json_data["priceWeight"])
        print(json_data["co2Weight"])
        print(json_data["adpfWeight"])

        return 1
