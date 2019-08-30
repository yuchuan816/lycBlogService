from .common import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'mysql.connector.django',
        'NAME': 'blog',
        'USER': 'yuchuan',
        'PASSWORD': '95816',
        'HOST': 'backend_mysql',
        'PORT': '3306',
    }
}