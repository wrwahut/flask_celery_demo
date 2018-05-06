from backend.app import flask_app, make_celery
from backend.common.conn_redis import Redisi

celery = make_celery(flask_app)

@celery.task()
def handle():
    Redisi().set_data("mykey111","12345678")
    print "%%%%%%%%%%%%%%%%%%%%%%%%"