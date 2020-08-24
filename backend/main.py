from flask import Flask, render_template, request
from flask_cors import CORS
from flask_jwt import JWT, jwt_required
from flask_restful import Api
from security import authenticate, identity
 
###ENDPOINTS (Resource)

#from endpoints.listusers import *
#from endpoints.getBom import *
#from endpoints.getKons import *
#from endpoints.getPersKons import *
#from endpoints.putKons import *
#from endpoints.putPersKons import *
#from endpoints.deleteKons import *
#from endpoints.deletePersKons import *
#from endpoints.getUser import *
#from endpoints.postKons import *
#from endpoints.getMara import *
from endpoints.getOrga import *
#from endpoints.getBomItem import *
from endpoints.getBomAl import *
from endpoints.getBranch import *
#from endpoints.getFunction import *
from endpoints.getReltyp import *
from endpoints.getFam import *
from endpoints.getComp import *
#from endpoints.getKons_test import *
from endpoints.getMaco import *
#from endpoints.getAllUser import *
from endpoints.getAllComp import *
from endpoints.user import UserPost, User, UserGet, Users
from endpoints.function import FunctionGet
from endpoints.reltyp import ReltypGet
from endpoints.branch import BranchGet
from endpoints.perp import PerpPost, Perp, PerpGet
from endpoints.kons import KonsPost, Kons, KonsGet
from endpoints.mara import MaraGet, MaraPost, Mara
from endpoints.BomItem import BomItemGet, BomItem, BomItemPost
from endpoints.BomAl import BomAlGet, BomAl, BomAlPost
from endpoints.orga import Orgas, Orga, OrgaPost
from endpoints.family import FamilyPost, Family, Families

# SETUP STEP

app = Flask(__name__)
CORS(app)

#####Norman Input#####
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop' 
#'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop' 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'bcdudes69_'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# User
api.add_resource(UserPost, '/user') # Post (registrieren)
api.add_resource(User, '/user/<string:_id>')# Put & Delete (ein User)
api.add_resource(UserGet, '/user/<string:e_mail>')# Get (ein User)
api.add_resource(Users, '/users') # Get (alle User)
# Auth
jwt = JWT(app, authenticate, identity)  # Endpoint /auth
# t_function
api.add_resource(FunctionGet, '/functions') #Alle Funktionen
# t_reltype
api.add_resource(ReltypGet, '/reltyps') #Alle Reltyps
# t_branch
api.add_resource(BranchGet, '/branches')#Alle Branchen
# Perp
api.add_resource(PerpPost, '/perp') #Post
api.add_resource(Perp, '/perp/<string:_id>') #Put & Delete
api.add_resource(PerpGet, '/perp/<string:kons_id>') #Get
# Kons
api.add_resource(KonsPost, '/kons') # Post
api.add_resource(Kons, '/kons/<string:_id>') #Put & Delete
api.add_resource(KonsGet, '/kons/<string:user_id>') #Get
# Mara
api.add_resource(MaraGet, '/mara/<string:user_id>') # Get
api.add_resource(MaraPost, '/mara') # Post
api.add_resource(Mara, '/mara/<string:_id>') # Put & Delete
# BomItem
api.add_resource(BomItemGet, '/bomitem/<string:mast_id>') #Get
api.add_resource(BomItemPost, '/bomitem') #Post
api.add_resource(BomItem, '/bomitem/<string:_id>') #Put & Delete
# BomAl
api.add_resource(BomAlGet, '/bomal/<string:kons_id>') #Get
api.add_resource(BomAl, '/bomal/<string:_id>') #Put & Delete
api.add_resource(BomAlPost, '/bomal') #Post
# Orga
api.add_resource(Orgas, '/orgas') #Alle Organisationen
api.add_resource(OrgaPost, '/orga') #Post
api.add_resource(Orga, '/orga/<string:_id>') #Put & Deleste
# Family
api.add_resource(Families, '/families') #Alle Familien
api.add_resource(FamilyPost, '/family') #Post
api.add_resource(Family, '/family/<string:_id>') #Put & Deleste

#api.add_resource(Kons, 'kons')


#if __name__ == '__main__':
#     from db import db
#     db.init_app(app)
#     app.run(port=5000, debug=True)

####Adrian Input######

#app.register_blueprint(listusers_bp)
#app.register_blueprint(getBom_bp)
#app.register_blueprint(getKons_bp)
#app.register_blueprint(getPersKons_bp)
#app.register_blueprint(putKons_bp)
#app.register_blueprint(putPersKons_bp)
#app.register_blueprint(deleteKons_bp)
#app.register_blueprint(deletePersKons_bp)
#app.register_blueprint(getUser_bp)
#app.register_blueprint(postKons_bp)
#app.register_blueprint(getMara_bp)
app.register_blueprint(getOrga_bp)
#app.register_blueprint(getBomItem_bp)
app.register_blueprint(getBomAl_bp)
app.register_blueprint(getBranch_bp)
#app.register_blueprint(getFunction_bp)
app.register_blueprint(getReltyp_bp)
app.register_blueprint(getFam_bp)
app.register_blueprint(getComp_bp)
#app.register_blueprint(getKons_test_bp)
app.register_blueprint(getMaco_bp)
#app.register_blueprint(getAllUser_bp)
#app.register_blueprint(User_bp)
app.register_blueprint(getAllComp_bp)


if __name__ == '__main__':
    from dbfunctions.connect import db
    db.init_app(app)
    app.run(host= '0.0.0.0',debug=True)
