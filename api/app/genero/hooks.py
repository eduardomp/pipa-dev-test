from .. import HOOKS
from flask import current_app as app
from werkzeug.exceptions import Conflict

def normaliza_nome_genero(genero):
    """
        Normaliza o nome do genero para string sem espacos em 
    """
    genero['nome'] = genero['nome'].strip().title()

    generoCollection = app.data.driver.db['genero']
    count = generoCollection.count_documents({'nome': genero['nome']})
    if count > 0 :
        raise Conflict("Genero já cadastrado!")

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
    items = map(normaliza_nome_genero, items)
    return list(items)

#adicionando os hooks a lista de hooks a serem registrados
HOOKS.append(on_insert_genero)