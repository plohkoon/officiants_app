
from flask import Blueprint

loginAPI = Blueprint('login_api', __name__)

@loginAPI.route("/", methods=["GET"])
def root():
    return "Login"