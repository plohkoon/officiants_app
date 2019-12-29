
from flask import Blueprint

privateAPI = Blueprint('private_api', __name__)

@privateAPI.route("/", methods=["GET"])
def root():
    return "private"