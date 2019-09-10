from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'yuchuan',
        'PASSWORD': '95816',
        'HOST': '129.204.76.142',
        'PORT': '3306'
    }
}
