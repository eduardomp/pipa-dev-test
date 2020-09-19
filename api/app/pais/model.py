from .. import DOMAIN

schema = {
    'iso':{
        'type': 'string',
        'required': True,
        'unique': True
    },
    'nome':{
        'type': 'string',
        'required': True,
        'unique': True
    },
    'nomeFormal':{
        'type': 'string',
        'required': True,
        'unique': True
    },
}

pais = {
    'resource_methods': ['GET'],
    'schema': schema
}

DOMAIN['pais'] = pais