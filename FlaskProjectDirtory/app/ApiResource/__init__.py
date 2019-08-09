from flask import Blueprint
from flask_restful import Api

api_main = Blueprint("api",__name__)

api = Api(api_main)

from . import ApiResource