from flask import Flask
from extensions import redis
from config import BaseConfig
from celery import Celery

flask_app = Flask(__name__)
flask_app.config.from_object(BaseConfig)
redis.init_app(flask_app)
redis.app = flask_app

def make_celery(app):
    print "############@@@@@@cofig=",app.config["CELERY_RESULT_BACKEND"]
    celery = Celery(
        app.import_name,
        broker = app.config["CELERY_BROKER_URL"],
        backend = app.config["CELERY_RESULT_BACKEND"]
    )
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery