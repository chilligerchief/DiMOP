from flask_restful import Resource, reqparse


class Search(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mat_desc',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('campus_fam',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('producer',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('verarbeitungsmethode',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('zugmodul',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('zugmodul_min',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('zugmodul_max',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('bruchspannung',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('bruchspannung_min',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('bruchspannung_max',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('bruchdehnung',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('bruchdehnung_min',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('bruchdehnung_max',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mvr',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mvr_min',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('mvr_max',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('dichte',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('dichte_min',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('dichte_max',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('belastung',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('belastung_min',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('belastung_max',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('temperatur',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('temperatur_min',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('temperatur_max',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )

    data = MatPost.parser.parse_args()

    def get(self):
        data = MatPost.parser.parse_args()
        print(data)
