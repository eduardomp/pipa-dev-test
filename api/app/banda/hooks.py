from .. import HOOKS
from flask import current_app as app
from werkzeug.exceptions import Conflict
import shortuuid

def gerar_codigo_banda(banda):
    """
        Gera um uuid curto (10 caracteres) como codigo interno
        das bandas, com prefixo 'B'

        ex: 'B8DVRViPNRo'
    """
    banda["codigo"] = "B"+shortuuid.ShortUUID().random(length=10)

    return banda

def on_insert_banda(items):
    """
        Hook de pre insercao das bandas.
    """
    items = list(map(gerar_codigo_banda, items))

    return items

#adicionando os hooks a lista de hooks a serem registrados
HOOKS.append(on_insert_banda)