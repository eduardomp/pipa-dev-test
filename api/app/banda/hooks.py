from .. import HOOKS
from flask import current_app as app
from werkzeug.exceptions import Conflict

def on_insert_banda(items):
    """
        Hook de pre insercao das bandas.
    """
    
    pass

#adicionando os hooks a lista de hooks a serem registrados
HOOKS.append(on_insert_banda)