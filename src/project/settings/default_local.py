# This file provides standard local development settings - to
# use, either symlink it as local_settings.py or import and
# override within your own local_settings.py file.

from .base import project_path, INSTALLED_APPS, DATABASES

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': project_path('cache'),
    }
}

INTERNAL_IPS = ['127.0.0.1']

RAVEN_CONFIG = {}

ALLOWED_HOSTS = ['127.0.0.1']
