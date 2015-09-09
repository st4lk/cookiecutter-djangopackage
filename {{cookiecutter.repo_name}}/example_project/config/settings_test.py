" Settings for tests. "
from .settings import *

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# celery, if any
CELERY_ALWAYS_EAGER = True
