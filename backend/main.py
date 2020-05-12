from flask import Flask, render_template, request
from flask_cors import CORS


from endpoints.listusers import *

# SETUP STEP


app = Flask(__name__)
CORS(app)

app.register_blueprint(listusers_bp)


if __name__ == '__main__':
    app.run()
