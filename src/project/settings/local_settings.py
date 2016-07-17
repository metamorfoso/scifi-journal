from .base import project_path, INSTALLED_APPS, DATABASES
from .default_local import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': project_path('scifi-journal-dev.db'),
    }
}
