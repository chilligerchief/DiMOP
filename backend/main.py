from flask import Flask, render_template, request
from flask_cors import CORS


from endpoints.listusers import *
from endpoints.getBom import *
from endpoints.getKons import *
from endpoints.getPersKons import *
from endpoints.updateKons import *
from endpoints.updatePersKons import *

# SETUP STEP

app = Flask(__name__)
CORS(app)

app.register_blueprint(listusers_bp)
app.register_blueprint(getBom_bp)
app.register_blueprint(getKons_bp)
app.register_blueprint(getPersKons_bp)
app.register_blueprint(updateKons_bp)
app.register_blueprint(updatePersKons_bp)


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
