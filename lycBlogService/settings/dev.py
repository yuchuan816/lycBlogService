from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_blog',
        'USER': 'developer',
        'PASSWORD': 'yuchuan816',
        'HOST': '180.76.248.62',
        'PORT': '3306'
    }
}
