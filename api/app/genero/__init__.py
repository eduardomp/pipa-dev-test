from flask import Blueprint
from .. import BLUEPRINTS

genero_bp = Blueprint('genero', __name__)

BLUEPRINTS.append(genero_bp)

from . import model
from . import views
