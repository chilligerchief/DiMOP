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

    def post(self):
        '''
        Returns recyclability.

        Args:
        - dmg_env: 1.0 if material damages environment
        - g: ?
        - h: ?

        Returns:
        - RV: Value for recyclability between 0.0 and 1.0
        '''
        data = Search.parser.parse_args()

        print("Test:")
        print(data)

        #data_list = []

        # for key in data:
        #    data_list.append([key, data[key]])

        #table_tree = pd.DataFrame(data_list, columns=['key', 'value'])
        #temp = table_tree.loc[table_tree["is_atomic"] == 1]

        #compability = pd.read_sql_query('SELECT * FROM compability', db_connection)
        #plast = pd.read_sql_query('SELECT * FROM plast', db_connection)
        #rel = pd.read_sql_query('SELECT * FROM rel', db_connection)

        #f1 = calculate_f1()
        #f2 = calculate_f2(temp)
        #f3 = calculate_f3(temp, rel, table_tree)
        #f4 = calculate_f4(temp, compability)

        # RV = f2 * f3 * f4 # * f1

        # print(RV)

        return {'evaluation': 'evaluation is working!'}
