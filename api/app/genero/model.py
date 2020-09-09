from .. import DOMAIN

schema = {
    'codigo':{
        'type': 'string',
        'unique': True
    },
    'nome':{
        'type': 'string',
        'required': True,
        'unique': True
    },
}

genero = {
    'schema': schema
}

DOMAIN['genero'] = genero