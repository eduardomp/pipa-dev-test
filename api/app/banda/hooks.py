from .. import HOOKS
from flask import current_app as app
from werkzeug.exceptions import Conflict
import shortuuid

def check_banda_existente(items):
    """
        Valida se já existe a banda informada,
        caso sim, um erro 409 é gerado
    """
    bandaCollection = app.data.driver.db['banda']
    
    for banda in items:

        count = bandaCollection.count_documents({'nome': banda['nome'],'pais':banda['pais'],'genero':banda['genero']})
        
        if count > 0 :
        
            raise Conflict(f"Banda ''{banda['nome']} - {banda['pais']} - {banda['genero']}'' já cadastrada!")

def normalizar_nome_banda(banda):
    """
        Normaliza o nome da banda retirando espacos em branco antes e apos
    """
    banda['nome'] = banda['nome'].strip()
    
    return banda

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
    items = list(map(normalizar_nome_banda, items))

    check_banda_existente(items)

    items = list(map(gerar_codigo_banda, items))

    return items

#adicionando os hooks a lista de hooks a serem registrados
HOOKS.append(on_insert_banda)