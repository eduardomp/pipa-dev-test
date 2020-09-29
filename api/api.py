from eve import Eve
from app import DOMAIN, BLUEPRINTS, HOOKS, SETTINGS, JOBS
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

def register_blueprints(api):
    if BLUEPRINTS:
        for blueprint in BLUEPRINTS:
            print(f'[API][BLUEPRINT] Registrando o blueprint {blueprint.name}')
            api.register_blueprint(blueprint)

def register_hooks(api):
    if HOOKS:
        for hook in HOOKS:
            print(f'[API][HOOK] Registrando o hook {hook.__name__}')
            #evita a injecao de codigo malicioso retirando as instrucoes default
            globalsParameter = {'__builtins__' : None}
            #apenas as variaveis api e hook podem ser executadas no contexto dinamico
            localsParameter = {'api': api, f'{hook.__name__}': hook}
            #execucao dinamica para registro dos hooks do Eve
            exec(f'api.{hook.__name__} += {hook.__name__}',globalsParameter,localsParameter)

def register_jobs(api):
    if JOBS: 
        print(f'[API][JOBS] {len(JOBS)} Jobs encontrados')
    
        #criar o scheduler para agendamento dos jobs
        scheduler = BackgroundScheduler()

        #itera pelos jobs cadastrados
        for job in JOBS:
            jobFunction = job.get('job',None)
            jobName = jobFunction.__name__
            hourOfExecution = job.get('hour',0) # 00:00 como hora default
            executeOnStartup = job.get('executeOnStartup', False)
            executeOnStartupOnly = job.get('executeOnStartupOnly', False)    

            if jobFunction == None:
                continue

            print(f'[API][JOBS] Registrando o job {jobName}')
            
            if executeOnStartup or executeOnStartupOnly:
                print(f'[API][JOBS] Executando o job {jobName} na inicialização conforme configurado...')
                jobFunction(api)
            
            #criar agendamento do job
            if executeOnStartupOnly != True:
                print(f'[API][JOBS] Agendando o job {jobName} para execução todos os dias as {hourOfExecution} ')
                scheduler.add_job(func=jobFunction,args=[api],trigger="cron", hour=hourOfExecution)

        scheduler.start()

        # Remove o scheduler quando a aplicação for terminada
        atexit.register(lambda: scheduler.shutdown())

api = Eve(settings=SETTINGS)

#registrando os modulos de forma dinamica
register_blueprints(api)

#registrando os hooks de forma dinamica
register_hooks(api)

#registrado os jobs
register_jobs(api)

if __name__ == '__main__':
    api.run(host= '0.0.0.0')