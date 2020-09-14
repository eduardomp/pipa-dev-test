#O domain sera definido dinamicamente em cada modulo
DOMAIN = {}

#A api sera dividida em blueprints do flask, registrados dinamicamente
BLUEPRINTS = []

#Registrar os HOOKS nesta lista para incrementar dinamicamente
HOOKS=[]

#Registrar jobs
JOBS=[]

#import dos settings
from . import config

SETTINGS = config.settings.get_settings()

#Import dos modulos, cada modulo define o seu domain, blueprint, testes e o que mais for pertinente ao modulo
from . import genero
