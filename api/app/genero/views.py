from flask import Blueprint
from .. import BLUEPRINTS
from flask import current_app as app
from werkzeug.exceptions import NotFound

genero_bp = Blueprint('genero', __name__)

BLUEPRINTS.append(genero_bp)

@genero_bp.route('/genero/codigo/<codigo>', methods=['GET'])
def get_por_codigo(codigo):

    generoCollection = app.data.driver.db['genero']

    genero = generoCollection.find_one({"codigo":str(codigo)})

    if genero == None:
        raise NotFound

    #convertendo o ObjectId do pymongo para string, tornando-o serializavel    
    genero['_id'] = str(genero['_id'])
    
    return genero
