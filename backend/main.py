from flask import Flask, render_template, request
from flask_cors import CORS
from flask_jwt import JWT, jwt_required
#from dbfunctions.connect import db
from flask_restful import Api

from security import authenticate, identity
 
###ENDPOINTS (Resource)

from endpoints.listusers import *
from endpoints.getBom import *
from endpoints.getKons import *
from endpoints.getPersKons import *
from endpoints.putKons import *
from endpoints.putPersKons import *
from endpoints.deleteKons import *
from endpoints.deletePersKons import *
from endpoints.getUser import *
from endpoints.postKons import *
from endpoints.getMara import *
from endpoints.getOrga import *
from endpoints.getBomItem import *
from endpoints.getBomAl import *
from endpoints.getBranch import *
from endpoints.getFunction import *
from endpoints.getReltyp import *
from endpoints.getFam import *
from endpoints.getComp import *
from endpoints.getKons_test import *
from endpoints.getMaco import *
from endpoints.getAllUser import *
from endpoints.user import UserRegister
from endpoints.getAllComp import *
# SETUP STEP

app = Flask(__name__)
#CORS(app)

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

jwt = JWT(app, authenticate, identity)  # Endpoint /auth

#api.add_resource(Store, '/store/<string:name>')
#api.add_resource(StoreList, '/stores')
#api.add_resource(Item, '/item/<string:name>')
#api.add_resource(Item, '/item')
api.add_resource(UserRegister, '/register')

#if __name__ == '__main__':
#     from db import db
#     db.init_app(app)
#     app.run(port=5000, debug=True)

####Adrian Input######

app.register_blueprint(listusers_bp)
app.register_blueprint(getBom_bp)
app.register_blueprint(getKons_bp)
app.register_blueprint(getPersKons_bp)
app.register_blueprint(putKons_bp)
app.register_blueprint(putPersKons_bp)
app.register_blueprint(deleteKons_bp)
app.register_blueprint(deletePersKons_bp)
app.register_blueprint(getUser_bp)
app.register_blueprint(postKons_bp)
app.register_blueprint(getMara_bp)
app.register_blueprint(getOrga_bp)
app.register_blueprint(getBomItem_bp)
app.register_blueprint(getBomAl_bp)
app.register_blueprint(getBranch_bp)
app.register_blueprint(getFunction_bp)
app.register_blueprint(getReltyp_bp)
app.register_blueprint(getFam_bp)
app.register_blueprint(getComp_bp)
app.register_blueprint(getKons_test_bp)
app.register_blueprint(getMaco_bp)
app.register_blueprint(getAllUser_bp)
#app.register_blueprint(User_bp)
app.register_blueprint(getAllComp_bp)


if __name__ == '__main__':
    from dbfunctions.connect import db
    db.init_app(app)
    app.run(host= '0.0.0.0',debug=True)
