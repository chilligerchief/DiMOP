"""
author: topr
last updated: 31.03.2021
currently used: yes
description: used to calculate recycling value
"""

from flask_restful import Resource, reqparse
import pandas as pd
import json
from dbfunctions.connect import connect_db


class Evaluation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mat_desc',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_id_int',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_desc_int',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('cad_id',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mara_plast_id',
                        type=int,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mat_rw',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('height',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('width',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('depth',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('unit',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('weight',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('weight_unit',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('volume',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('volume_unit',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('is_atomic',
                        type=int,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('orga_id',
                        type=int,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('cons_id',
                        type=int,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('del_kz',
                        type=int,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('price',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('co2_value',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('resource_use',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
