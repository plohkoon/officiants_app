import flask

from login import loginAPI
from public import publicAPI
from private import privateAPI

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(loginAPI, url_prefix="/login")
app.register_blueprint(publicAPI, url_prefix="/public")
app.register_blueprint(privateAPI, url_prefix="/private")

@app.route('/', methods=["GET"])
def home():
    return "Hello World"

app.run()