from eve import Eve
from app import DOMAIN, BLUEPRINTS, HOOKS, SETTINGS

def register_blueprints(api):
    for blueprint in BLUEPRINTS:
        print(f'[API][MODULO] Registrando o modulo {blueprint.name}')
        api.register_blueprint(blueprint)

def register_hooks(api):
    for hook in HOOKS:
        print(f'[API][HOOK] Registrando o hook {hook.__name__}')
        #evita a injecao de codigo malicioso retirando as instrucoes default
        globalsParameter = {'__builtins__' : None}
        #apenas as variaveis api e hook podem ser executadas no contexto dinamico
        localsParameter = {'api': api, 'hook': hook}
        #execucao dinamica para registro dos hooks do Eve
        exec(f'api.{hook.__name__} += hook',globalsParameter,localsParameter)

api = Eve(settings=SETTINGS)

#registrando os modulos de forma dinamica
register_blueprints(api)

#registrando os hooks de forma dinamica
register_hooks(api)

if __name__ == '__main__':
    api.run()