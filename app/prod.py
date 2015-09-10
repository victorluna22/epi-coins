from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'epicoins',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'epicoins',
        'PASSWORD': 'epi.coins',
        'HOST': 'epicoins.c3asbzcdo0qt.us-east-1.rds.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

STATIC_ROOT = '/u/web/dev/statics/static/'