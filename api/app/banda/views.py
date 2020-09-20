from flask import Blueprint
from .. import BLUEPRINTS

banda_bp = Blueprint('banda', __name__)

BLUEPRINTS.append(banda_bp)

@banda_bp.route('/banda/test', methods=['GET'])
def get_test():
    return "TESTE MODULARIZACAO COM BLUEPRINTS"
