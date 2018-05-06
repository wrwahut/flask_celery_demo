class BaseConfig(object):
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
    REDIS_ENABLED = True
    REDIS_URL = "redis://localhost:6379"
    REDIS_DATABASE = 0