from .common import *

# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'yuchuan',
        'PASSWORD': '95816',
        'HOST': 'backend_mysql',
        'PORT': '3306'
    }
}
