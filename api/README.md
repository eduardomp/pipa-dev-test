# Api

Api do desafio 

## Pré requisitos

- python 3.6+ 
- mongodb 
- poetry (dependency management)
- docker (opcional)

## rodando o mongodb com docker

```
docker run --name pipa-dev-test -d mongo

```

## Executando a api para desenvolvimento

Acesse o diretorio do projeto api e instale as dependencias utilizando o poetry:

```
poetry install

```

Neste momento todas as dependencias do projeto serão instaladas em um ambiente virtual do python. 

Para rodar o projeto, execute: 

```
#entre no shell do virtualenv criado pelo poetry

poetry shell

# execute a api
python api.py

```

O projeto da api estara disponivel em http://localhost:5000







