from .. import JOBS
import requests
from bs4 import BeautifulSoup
import shortuuid

def sincronizar_generos(app):
    
    print("[API][JOB]Sincronizando generos da pagina https://musicbrainz.org/genres")

    #pegar a pagina com o beatifulsoup
    
    #definindo os headers da conexão
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    #url de onde pegaremos os generos musicais
    url = "https://musicbrainz.org/genres"
    
    #requisicao GET a pagina da url
    req = requests.get(url, headers)
    
    #criando o parser para navegar no DOM da pagina e extrair os valores
    soup = BeautifulSoup(req.content, 'html.parser')
    
    #select css para pegar cada item da lista de generos
    items = soup.select("#content > ul > li")

    with app.app_context():
    
        #recuperar o objeto de collection de generos
        generoCollection = app.data.driver.db['genero']

        generos=[]
        #iterar pelos itens, capturar o MBID (Muzic Brains ID) e o nome do genero
        for item in items:
            codigo = shortuuid.uuid()
            nome = item.find('bdi').get_text().strip().title()

            count = generoCollection.count_documents({'nome': nome})
        
            #inserir o genero caso nao exista
            if count == 0 :    
                generos.append({"codigo":codigo,"nome":nome})

        if generos:
            generoCollection.insert_many(generos)                

    #mensagem de ok
    print("[API][JOB]Generos sincronizados!")

JOBS.append({"job":sincronizar_generos,"hour":2,"executeOnStartup":True})