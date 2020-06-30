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



if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
