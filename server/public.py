
from flask import Blueprint

publicAPI = Blueprint('public_api', __name__)

@publicAPI.route("/", methods=["GET"])
def root():
    return "public"