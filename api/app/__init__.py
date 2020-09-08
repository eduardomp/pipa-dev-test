from eve import Eve

#settings como dict

settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'api',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'DOMAIN': {}
}

#import dos modulos
from . import genero

app = Eve(settings=settings)

#registro dos blueprints
app.register_blueprint(genero.genero_bp)
