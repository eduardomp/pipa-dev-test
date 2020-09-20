from .. import DOMAIN

schema = {
    'nome':{
        'type': 'string',
        'required': True,
        'unique': False
    },
    'pais': {
        'type': 'string',
        'data_relation': {
            'resource': 'pais',
            'field': 'iso',
            'embeddable': True,
        },
    },
    'genero': {
        'type': 'string',
        'data_relation': {
            'resource': 'genero',
            'field': 'codigo',
            'embeddable': True,
        },
    },
}

banda = {
    'schema': schema
}

DOMAIN['banda'] = banda