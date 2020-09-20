from flask import Blueprint
from .. import BLUEPRINTS
from flask import current_app as app
from werkzeug.exceptions import NotFound

banda_bp = Blueprint('banda', __name__)

BLUEPRINTS.append(banda_bp)

@banda_bp.route('/banda/<codigo>', methods=['GET'])
def get_por_codigo(codigo):

    bandaCollection = app.data.driver.db['banda']

    banda = bandaCollection.find_one({"codigo":str(codigo)})

    if banda == None:
        raise NotFound

    #convertendo o ObjectId do pymongo para string, tornando-o serializavel    
    banda['_id'] = str(banda['_id'])
    
    return banda