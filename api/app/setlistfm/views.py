from flask import Blueprint
from .. import BLUEPRINTS
import requests
from urllib import parse

setlistfm_bp = Blueprint('setlistfm', __name__)

BLUEPRINTS.append(setlistfm_bp)

BASE_URL = 'https://api.setlist.fm/rest'

#definindo os headers da conexão com setlist.fm
HEADERS = {
    'x-api-key':'JorcwOqolsbPsFkEAAwkydlKcysTBXfyiuzg',
    'Accept-Language':'pt',
    'Accept':'application/json',
}

@setlistfm_bp.route('/setlistfm/artista/<nome>', methods=['GET'])
def buscar_por_nome(nome):

    nome_pesquisa = parse.quote(nome)

    endpoint = f'{BASE_URL}/1.0/search/artists?p=1&sort=relevance&artistName={nome_pesquisa}'

    response = requests.get(endpoint,headers=HEADERS)    

    return response.json()