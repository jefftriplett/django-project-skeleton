import os

from .base import *


DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_ROOT, "dev.db"),
    },
}

PREREQ_APPS += [
    'django_coverage',
    'django_jenkins',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS
