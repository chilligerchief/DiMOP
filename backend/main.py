from flask import Flask, render_template, request
from flask_cors import CORS
from flask_jwt import JWT, jwt_required
from flask_restful import Api
from security import authenticate, identity

###ENDPOINTS (Resource)
from endpoints.user import UserPost, User, UserGet, Users, ChangePassword
from endpoints.function import FunctionGet
from endpoints.reltyp import ReltypGet
from endpoints.branch import BranchGet
from endpoints.perp import PerpPost, Perp, PerpGet
from endpoints.kons import KonsPost, Kons, KonsGet
from endpoints.cons import ConsPost, Cons, ConsGet
from endpoints.mara import MaraGet, MaraPost, Mara
from endpoints.plast import PlastGet, Plast
from endpoints.BomItem import BomItemGet, BomItem, BomItemPost
from endpoints.mat import MatGet, Mat, MatPost
from endpoints.BomAl import BomAlGet, BomAl, BomAlPost
from endpoints.orga import Orgas, Orga, OrgaPost
from endpoints.family import FamilyPost, Family, Families
from endpoints.maco import MacoGet, MacoPost, Maco
from endpoints.comp import CompGet, CompPost, Comp
from endpoints.origin import OriginGet
from endpoints.tabletree import Tabletree
from endpoints.bom import Bom, BomAlter
from endpoints.topsis import TopsisTobi

#from Topsis_Milena.topsis_endpoint import Topsis

from endpoints.test import Test
from endpoints.search import Search
from endpoints.search import Results

# SETUP STEP
app = Flask(__name__)
CORS(app)

#####Norman Input#####
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop'
# 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'bcdudes69_'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


# Auth
jwt = JWT(app, authenticate, identity)  # Auth
# t_function
api.add_resource(FunctionGet, '/functions')  # Alle Funktionen
# tabletree
api.add_resource(Tabletree, '/tree/<int:mat_id>')
# topsis
api.add_resource(TopsisTobi, '/topsis')
# t_reltype
api.add_resource(ReltypGet, '/reltyps')  # Alle Reltyps
# t_branch
api.add_resource(BranchGet, '/branches')  # Alle Branchen
# t_origin
api.add_resource(OriginGet, '/origins')  # Alle Origings der Comp-values
# User
api.add_resource(UserPost, '/user')  # Post (Registrierung)
api.add_resource(User, '/user/<string:_id>')  # Put & Delete (ein User)
api.add_resource(UserGet, '/user/<string:_id>')  # Get (ein User)
api.add_resource(Users, '/users')  # Get (alle User)
api.add_resource(ChangePassword, '/password/<string:_id>')  # Put User-Passwort
# Perp
api.add_resource(PerpPost, '/perp')  # Post
api.add_resource(Perp, '/perp/<string:_id>')  # Put & Delete
api.add_resource(PerpGet, '/perp/<string:kons_id>')  # Get
# Kons
api.add_resource(KonsPost, '/kons')  # Post
api.add_resource(Kons, '/kons/<string:_id>')  # Put & Delete
api.add_resource(KonsGet, '/kons/<string:user_id>')  # Get
# Cons
api.add_resource(ConsPost, '/cons')  # Post
api.add_resource(Cons, '/cons/<string:_id>')  # Put & Delete
api.add_resource(ConsGet, '/cons/<string:orga_id>')  # Get
# Mara
api.add_resource(MaraGet, '/mara/<string:user_id>')  # Get
api.add_resource(MaraPost, '/mara')  # Post
api.add_resource(Mara, '/mara/<string:_id>')  # Put & Delete
# Plast
api.add_resource(PlastGet, '/plast')  # Get
api.add_resource(Plast, '/plast/<string:_id>')  # Put & Delete
# BomItem
api.add_resource(BomItemGet, '/bomitem/<string:mast_id>')  # Get
api.add_resource(BomItemPost, '/bomitem')  # Post
api.add_resource(BomItem, '/bomitem/<string:_id>')  # Put & Delete
# Mat
api.add_resource(MatGet, '/mat')  # Get
api.add_resource(MatPost, '/mat')  # Post
api.add_resource(Mat, '/mat/<string:_id>')  # Put & Delete
# BomAl
api.add_resource(BomAlGet, '/bomal/<string:kons_id>')  # Get
api.add_resource(BomAl, '/bomal/<string:_id>')  # Put & Delete
api.add_resource(BomAlPost, '/bomal')  # Post
# Orga
api.add_resource(Orgas, '/orgas')  # Alle Organisationen
api.add_resource(OrgaPost, '/orga')  # Post
api.add_resource(Orga, '/orga/<string:_id>')  # Put & Deleste
# Family
api.add_resource(Families, '/families')  # Alle Familien
api.add_resource(FamilyPost, '/family')  # Post
api.add_resource(Family, '/family/<string:_id>')  # Put & Deleste
# Maco
api.add_resource(MacoGet, '/maco/<string:stpo_id>')  # Get
api.add_resource(MacoPost, '/maco')  # Post
api.add_resource(Maco, '/maco/<string:_id>')  # Put & Deleste
# Comp
api.add_resource(CompGet, '/comp/<string:t_fam_id>')  # Get
api.add_resource(CompPost, '/comp')  # Post
api.add_resource(Comp, '/comp/<string:_id>')  # Put & Deleste
# Bom
#api.add_resource(BomGet, '/bom')
#api.add_resource(BomPost, '/bom')
#api.add_resource(Bom, '/bom/<string:_id>')
api.add_resource(Bom, '/bom')
api.add_resource(BomAlter, '/bom/<string:_id>')

api.add_resource(Search, '/search/<string:criteria>')
api.add_resource(Results, '/results')

api.add_resource(Test, "/test")


if __name__ == '__main__':
    from dbfunctions.connect import db
    db.init_app(app)
    app.run(host='0.0.0.0', debug=True)

# Altes Format Main
# app.register_blueprint(listusers_bp) # als altes Beispiel beibehalten
# if __name__ == '__main__':
#     from db import db
#     db.init_app(app)
#     app.run(port=5000, debug=True)
