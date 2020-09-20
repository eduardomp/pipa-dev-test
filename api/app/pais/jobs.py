from .. import JOBS
import os
import sys
import json

def cadastrar_paises(app):
    
    print("[API][JOB] Populando a collections de paises...")

    arquivoJson = os.path.join(os.path.dirname(__file__), 'countriesJson_ptBR.json')

    paises = []

    with open(arquivoJson,'r') as arquivo:
        paises = json.load(arquivo)

    with app.app_context():
    
        #recuperar o objeto de collection de paises
        paisCollection = app.data.driver.db['pais']

        count = paisCollection.count_documents({})
        
        print(f"[API][JOB] {count} Paises encontrados!")

        if count == 0 :    
            paisCollection.insert_many(paises)                
            #mensagem de ok
            print(f"[API][JOB] {len(paises)} Paises cadastrados!")
    

JOBS.append({"job":cadastrar_paises,"executeOnStartupOnly":True})