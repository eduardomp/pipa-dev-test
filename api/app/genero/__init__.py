from flask import Blueprint, current_app as app

genero_bp = Blueprint('prefix_uri', __name__)

from . import model
from . import views
