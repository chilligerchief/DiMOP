from flask import Flask, render_template, request
from flask_cors import CORS


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
from endpoints.getUsers import *
from endpoints.getOrga import *
from endpoints.getBomItem import *
from endpoints.getBomAl import *
from endpoints.getBranch import *
from endpoints.getFunction import *
from endpoints.getReltyp import *
from endpoints.getFam import *

# SETUP STEP

app = Flask(__name__)
CORS(app)

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
app.register_blueprint(getUsers_bp)
app.register_blueprint(getOrga_bp)
app.register_blueprint(getBomItem_bp)
app.register_blueprint(getBomAl_bp)
app.register_blueprint(getBranch_bp)
app.register_blueprint(getFunction_bp)
app.register_blueprint(getReltyp_bp)
app.register_blueprint(getFam_bp)



if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
