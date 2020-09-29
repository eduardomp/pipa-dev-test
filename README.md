
# Repositorio do projeto, desafio vida segura

Estrutura do repositorio

```
.
├── api                 # Aplicação da API (Python3, Eve, Poetry)
├── docker-compose.yml  # Docker compose
├── frontend            # Aplicação Vue 
└── README.md

```

# Docker Compose

O projeto esta configurado para rodar dentro de containers docker, coordenados pelo docker compose. Verifique a instalação do docker e do docker compose em sua maquina e execute o seguinte comando na raiz do repositorio:

```
docker-compose up

```

Apos a criação das imagens e execução dos containers  (mongo, api e front) a aplicação ficará disponivel em http://localhost:8080

A seguir temos instruções e detalhes sobre os projetos api e frontend

# Api

Api do desafio 

## Pré requisitos

- python 3.6+ 
- mongodb 
- poetry (dependency management)
- docker (opcional)

## Executando a api individualmente

## rodando o mongodb com docker 

```
docker run -d --name pipa-dev-test -p 27017:27017 mongo

```

## Executando a api para desenvolvimento

Acesse o diretorio /api do projeto e instale as dependencias utilizando o poetry:

```
# instale as dependencias
poetry install

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

# detalhes do projeto API

```
.
├── api.py                           # Ponto de entrada 
├── app                              # Modulo principal da aplicacao 
│   ├── __init__.py                  # Definição do Modulo de principal
│   ├── banda                        # Modulo do dominio "Banda" da aplicacao 
│   │   ├── hooks.py                 # Hooks do Eve para o dominio "Banda"
│   │   ├── __init__.py              # declaração do modulo "Banda"
│   │   ├── model.py                 # Definição do dominio "Banda"
│   │   ├── tests.py                 # Testes unitarios do dominio "Banda"
│   │   └── views.py                 # Endpoints flask personalizados
│   ├── config                       # Modulo de configuração
│   │   ├── __init__.py              # Definição do Modulo de configuração
│   │   └── settings.py              # Configuração do EVE
│   ├── genero                       # Modulo do dominio "Genero" da aplicacao 
│   │   ├── hooks.py                 # Hooks do Eve para o dominio "Genero"
│   │   ├── __init__.py              # declaração do modulo "Genero"
│   │   ├── jobs.py                  # Jobs APS para execução de tarefas (scrapper)
│   │   ├── model.py                 # Definição do dominio "Genero"
│   │   ├── tests.py                 # Testes unitarios do dominio "Genero"
│   │   └── views.py                 # Endpoints flask personalizados
│   ├── pais                         # Modulo do dominio "Pais" da aplicacao 
│   │   ├── countriesJson_ptBR.json  # Arquivo json para carga de dados dos paises
│   │   ├── __init__.py              # declaração do modulo "Pais"
│   │   ├── jobs.py                  # Jobs APS para execução de tarefas (carga do banco)
│   │   ├── model.py                 # Definição do dominio "Pais"
│   │   └── views.py                 # Endpoints flask personalizados
│   └── setlistfm                    # Modulo de integração com a api setlistfm.com
│       ├── __init__.py              # declaração do modulo "setlistfm" 
│       └── views.py                 # Endpoints flask personalizados
├── Dockerfile                       # Arquivo de definição do container docker da api
├── poetry.lock                      # Arquivo para travar as dependencias do projeto 
├── pyproject.toml                   # Arquivo de configuração usado pelo Poetry
└── tox.ini                          # Arquivo de configuração usado pelo Tox

```

# Jobs

Para este projeto foi utilizado o APS (Advanced Python Scheduler) para execução de jobs agendados ou no momento da inicialização da aplicação.

A aplicação ao ser iniciada, sincroniza os generos cadastrados com o site musicbrainz.org e agenda a mesma sincronização para todos os dias as 2 AM.

Outro job executado na inicialização se encarrega de carregar os paises no banco de dados.

# Frontend

O frontend foi implementado em Vue utilizando o package manager Yarn. Para execução local execute os comandos a seguir:

```
# instalando as dependencias
yarn install

# executando o projeto
yarn serve

```

O projeto ficará disponivel em http://localhost:8080
