from .. import HOOKS

def on_pre_GET_genero(request, lookup):
    print('Hook de GET no genero funcionando!')

def on_pre_POST_genero(request, lookup):
    print('Hook de POST no genero funcionando!')

HOOKS.append(on_pre_GET_genero)
HOOKS.append(on_pre_POST_genero)