from eve import Eve
from app import DOMAIN, BLUEPRINTS

settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'api',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'DOMAIN': DOMAIN
}

def register_blueprints(api):
    for blueprint in BLUEPRINTS:
        print(f'[API] Registrando o modulo {blueprint.name}')
        api.register_blueprint(blueprint)

api = Eve(settings=settings)

register_blueprints(api)

if __name__ == '__main__':
    api.run()