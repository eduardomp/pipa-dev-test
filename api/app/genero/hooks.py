from .. import HOOKS
from flask import current_app as app
from werkzeug.exceptions import Conflict
import shortuuid

def check_genero_existente(items):
    """
        Valida se já existe o genero informado,
        caso sim, um erro 409 é gerado
    """
    generoCollection = app.data.driver.db['genero']
    
    for genero in items:

        count = generoCollection.count_documents({'nome': genero['nome']})
        
        if count > 0 :
        
            raise Conflict("Genero já cadastrado!")

def  normaliza_nome_genero(genero):
    """
        Normaliza o nome do genero para string sem espacos no inicio e no final,
        bem como ajuste das iniciais dos termos em maiusculo. 
    """
    genero['nome'] = genero['nome'].strip().title()

    return genero

def gerar_codigo_genero(genero):
    """
        Gera um uuid curto (10 caracteres) como codigo interno
        dos generos, com prefixo 'G'

        ex: 'G8DVRViPNRo'
    """
    genero["codigo"] = "G"+shortuuid.ShortUUID().random(length=10)

    return genero

def on_insert_genero(items):
    """
        Hook de pre insercao dos generos musicais.
        
        Este hook normaliza o nome, retirando os espacos em branco do inicio e do fim da string
        bem como padroniza as palavras para iniciais maiusculas.
         Ex: 
            Nome enviado: " heAvy meTAL  "
            Nome padronizado: "Heavy Metal"

        Com isso, evitamos duplicidade no banco , pois nome esta como 'unique' na definicao do schema.
    """
    items = list(map(normaliza_nome_genero, items))
    
    check_genero_existente(items)
    
    items = list(map(gerar_codigo_genero, items))
    
    return items

def on_delete_item_genero(item):
    """
        Hook de pre delecao dos generos musicais.

        Este hook deleta as bandas associadas ao genero excluido antes de excluir o genero        
    """
    bandaCollection = app.data.driver.db['banda']

    bandaCollection.delete_many({"genero":item.get('_id')})

    return item


#adicionando os hooks a lista de hooks a serem registrados
HOOKS.append(on_delete_item_genero)
HOOKS.append(on_insert_genero)