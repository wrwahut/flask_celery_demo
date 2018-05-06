# flask_celery_demo
use celery with the flask context, the demo have no db operator just with redis


## step: open three terminals（your redis server is opening,if not please run redis-server）
### first: start celery command as:
        celery -A celery_worker worker -l info
### second: start flask application ,the command is :
        python run.py
### final: run the bash command 
        curl https://localhost:9000/index
        
