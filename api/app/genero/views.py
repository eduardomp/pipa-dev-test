from . import genero_bp

@genero_bp.route('/genero/test', methods=['GET'])
def get_test():
    return "TESTE MODULARIZACAO COM BLUEPRINTS"
