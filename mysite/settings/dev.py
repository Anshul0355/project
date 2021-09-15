from .base import *
DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'mysite',
        'USER' : 'postgres',
        'PASSWORD' : 'psql',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}