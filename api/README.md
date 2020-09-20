# Api

Api do desafio 

## Pré requisitos

- python 3.6+ 
- mongodb 
- poetry (dependency management)
- docker (opcional)

## rodando o mongodb com docker

```
docker run -d --name pipa-dev-test -p 27017:27017 mongo

```

## Executando a api para desenvolvimento

Acesse o diretorio /api do projeto e instale as dependencias utilizando o poetry:

```
poetry install

```

Neste momento todas as dependencias do projeto serão instaladas em um ambiente virtual do python. 

```
# execute a api
poetry run python api.py

```

O projeto da api estara disponivel em http://localhost:5000

# Dados de acesso a api setlist.fm

Dados             | Valor
------------------|------------------------------------------
Email de contato  |	edu.medeirospereira@gmail.com
Descrição         |	Test application to new pipa developers
API Key           | JorcwOqolsbPsFkEAAwkydlKcysTBXfyiuzg
