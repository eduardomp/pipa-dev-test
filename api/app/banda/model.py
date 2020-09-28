from .. import DOMAIN

schema = {
    'nome':{
        'type': 'string',
        'required': True,
        'unique': False
    },
    'codigo':{
        'type': 'string',
        'unique': True
    },
    'pais': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'pais',
            'field': '_id',
            'embeddable': True,
        },
    },
    'genero': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'genero',
            'field': '_id',
            'embeddable': True,
        },
    },
}

banda = {
    'schema': schema
}

DOMAIN['banda'] = banda