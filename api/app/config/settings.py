import os
from .. import DOMAIN

__default_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'api',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'X_DOMAINS': '*',
    'X_HEADERS': ['Authorization','Content-type','Access-Control-Allow-Origin'],
    'MONGO_QUERY_BLACKLIST': ['$where'],
    'DOMAIN': DOMAIN
}

__prod_settings = {
    'MONGO_HOST': os.environ.get('MONGO_HOST'),
    'MONGO_PORT': os.environ.get('MONGO_PORT'),
    'MONGO_DBNAME': 'api',
    'MONGO_USERNAME': os.environ.get('MONGO_USER'),
    'MONGO_PASSWORD': os.environ.get('MONGO_PASS'),
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'X_DOMAINS': '*',
    'X_HEADERS': ['Authorization','Content-type','Access-Control-Allow-Origin'],
    'MONGO_QUERY_BLACKLIST': ['$where'],
    'DOMAIN': DOMAIN
}

def get_settings():
    if os.environ.get('API_ENVIRONMENT') == 'PROD':
        print('[API][CONFIG] Ambiente de produção')
        return __prod_settings
    else:
        print('[API][CONFIG] Ambiente de desenvolvimento')
        return __default_settings
 