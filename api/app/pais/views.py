from flask import Blueprint
from .. import BLUEPRINTS
from flask import current_app as app
from werkzeug.exceptions import NotFound

pais_bp = Blueprint('pais', __name__)

BLUEPRINTS.append(pais_bp)

@pais_bp.route('/pais/<iso>', methods=['GET'])
def get_por_iso(iso):

    paisCollection = app.data.driver.db['pais']

    pais = paisCollection.find_one({"iso":str(iso)})

    if pais == None:
        raise NotFound

    #convertendo o ObjectId do pymongo para string, tornando-o serializavel    
    pais['_id'] = str(pais['_id'])
    
    return pais
