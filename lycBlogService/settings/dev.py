from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'yuchuan',
        'PASSWORD': '95816',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
