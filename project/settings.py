import os
import dj_database_url
import environs

env = environs.Env()
env.read_env()

DATABASES = {
    'default': dj_database_url.config(
            default='postgres://...',
            conn_max_age=600,
            conn_health_checks=True,)

    }

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv("SECRET_KEY", "REPLACE_ME")

DEBUG = env.bool("DEBUG", False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", ['localhost',
                                            '127.0.0.1'])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATIC_URL = '/static/'

STATICFILES_DIRS = ['static/']

STATIC_ROOT = 'collected_static'