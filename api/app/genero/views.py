from flask import Blueprint
from .. import BLUEPRINTS

genero_bp = Blueprint('genero', __name__)

BLUEPRINTS.append(genero_bp)

@genero_bp.route('/genero/test', methods=['GET'])
def get_test():
    return "TESTE MODULARIZACAO COM BLUEPRINTS"
