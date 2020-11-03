from flask_restful import Resource, reqparse


class Search(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('t1',
    #                     type=str,
    #                     # required=True,
    #                     # help="This field cannot be blank."
    #                     )
    # parser.add_argument('t2',
    #                     type=int,
    #                     # required=True,
    #                     # help="This field cannot be blank."
    #                     )

    def get(self, criteria):

        if (criteria.lower() == "zugmodul"):
            return {
                "Zugmodul_MPa_trocken": {"min": 0, "max": 8},
                "Zugmodul_MPa_konditioniert": {"min": 0, "max": 10},
                "Zugmodul_Kriech_1h_MPa_trocken": {"min": 0, "max": 20},
                "Zugmodul_Kriech_1h_MPa_konditioniert": {"min": 0, "max": 12},
                "Zugmodul_Kriech_1000h_MPa_trocken": {"min": 0, "max": 16},
                "Zugmodul_Kriech_1000h_MPa_konditioniert": {"min": 0, "max": 14},
                "Zugmodul_Parallel_MPa_trocken": {"min": 0, "max": 15},
                "Zugmodul_Parallel_MPa_konditioniert": {"min": 0, "max": 13},
                "Zugmodul_Senkrecht_MPa_trocken": {"min": 0, "max": 17},
                "Zugmodul_Senkrecht_MPa_konditioniert": {"min": 0, "max": 9},
            }
        elif criteria.lower() == "bruchdehnung":
            return {
                "Bruchdehnung_trocken": {"min": 0, "max": 8},
                "Bruchdehnung_konditioniert": {"min": 0, "max": 10},
                "Bruchdehnung_Nominell_trocken": {"min": 0, "max": 20},
                "Bruchdehnung_Nominell_konditioniert": {"min": 0, "max": 12},
                "Bruchdehnung_TPE_trocken": {"min": 0, "max": 16},
                "Bruchdehnung_TPE_konditioniert": {"min": 0, "max": 14},
                "Bruchdehnung_Parallel_trocken": {"min": 0, "max": 15},
                "Bruchdehnung_Parallel_konditioniert": {"min": 0, "max": 13},
            }
        else:  # placeholder for now
            return {
                "Zugmodul_MPa_trocken": {"min": 0, "max": 8},
                "Zugmodul_MPa_konditioniert": {"min": 0, "max": 10},
                "Zugmodul_Kriech_1h_MPa_trocken": {"min": 0, "max": 20},
                "Zugmodul_Kriech_1h_MPa_konditioniert": {"min": 0, "max": 12},
                "Zugmodul_Kriech_1000h_MPa_trocken": {"min": 0, "max": 16},
                "Zugmodul_Kriech_1000h_MPa_konditioniert": {"min": 0, "max": 14},
                "Zugmodul_Parallel_MPa_trocken": {"min": 0, "max": 15},
                "Zugmodul_Parallel_MPa_konditioniert": {"min": 0, "max": 13},
                "Zugmodul_Senkrecht_MPa_trocken": {"min": 0, "max": 17},
                "Zugmodul_Senkrecht_MPa_konditioniert": {"min": 0, "max": 9},
            }


class Results(Resource):

    # parser.add_argument('t1',
    #                     type=str,
    #                     # required=True,
    #                     # help="This field cannot be blank."
    #                     )
    # parser.add_argument('t2',
    #                     type=str
    #                     # required=True,
    #                     # help="This field cannot be blank."
    #
    # )

    parser = reqparse.RequestParser()

    parser.add_argument("id", type=int)
    parser.add_argument("mat_desc", type=str)
    parser.add_argument("mat_int_desc", type=str)
    parser.add_argument("t_fam_id", type=str)
    parser.add_argument("campus_fam", type=str)
    parser.add_argument("t_mara_art_id", type=str)
    parser.add_argument("upload_kind", type=str)
    parser.add_argument("created_at", type=str)
    parser.add_argument("updated_at", type=str)
    parser.add_argument("unit", type=str)
    parser.add_argument("del_kz", type=str)
    parser.add_argument("producer", type=str)
    parser.add_argument("Verarbeitungsmethode", type=str)
    parser.add_argument("dichte_trocken", type=str)
    parser.add_argument("dichte_konditioniert", type=str)
    parser.add_argument("Belastung_trocken", type=str)
    parser.add_argument("Belastung_konditioniert", type=str)
    parser.add_argument("Temperatur_trocken", type=str)
    parser.add_argument("Temperatur_konditioniert", type=str)
    parser.add_argument("MVR_trocken", type=str)
    parser.add_argument("MVR_konditioniert", type=str)
    parser.add_argument("Bruchdehnung_trocken", type=str)
    parser.add_argument("Bruchdehnung_konditioniert", type=str)
    parser.add_argument("Bruchdehnung_Nominell_trocken", type=str)
    parser.add_argument("Bruchdehnung_Nominell_konditioniert", type=str)
    parser.add_argument("Bruchdehnung_TPE_trocken", type=str)
    parser.add_argument("Bruchdehnung_TPE_konditioniert", type=str)
    parser.add_argument("Bruchdehnung_Parallel_trocken", type=str)
    parser.add_argument("Bruchdehnung_Parallel_konditioniert", type=str)
    parser.add_argument("Bruchspannung_MPa_trocken", type=str)
    parser.add_argument("Bruchspannung_MPa_konditioniert", type=str)
    parser.add_argument("Bruchspannung_TPE_MPa_trocken", type=str)
    parser.add_argument("Bruchspannung_TPE_MPa_konditioniert", type=str)
    parser.add_argument("Bruchspannung_Parallel_MPa_trocken", type=str)
    parser.add_argument("Bruchspannung_Parallel_MPa_konditioniert", type=str)
    parser.add_argument("Bruchspannung_Senkrecht_MPa_trocken", type=str)
    parser.add_argument("Bruchspannung_Senkrecht_MPa_konditioniert", type=str)
    parser.add_argument("Zugmodul_MPa_trocken", type=str)
    parser.add_argument("Zugmodul_MPa_konditioniert", type=str)
    parser.add_argument("Zugmodul_Kriech_1h_MPa_trocken", type=str)
    parser.add_argument("Zugmodul_Kriech_1h_MPa_konditioniert", type=str)
    parser.add_argument("Zugmodul_Kriech_1000h_MPa_trocken", type=str)
    parser.add_argument("Zugmodul_Kriech_1000h_MPa_konditioniert", type=str)
    parser.add_argument("Zugmodul_Parallel_MPa_trocken", type=str)
    parser.add_argument("Zugmodul_Parallel_MPa_konditioniert", type=str)
    parser.add_argument("Zugmodul_Senkrecht_MPa_trocken", type=str)
    parser.add_argument("Zugmodul_Senkrecht_MPa_konditioniert", type=str)

    def get(self):
        args = self.parser.parse_args()
        print(args['id'])
        print(args['mat_desc'])
        print(args['mat_int_desc'])
