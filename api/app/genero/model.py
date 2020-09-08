from .. import settings

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

settings['DOMAIN']['genero'] = genero