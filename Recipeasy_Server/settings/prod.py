from .base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ['recipeasy.link', '127.0.0.1:8000', '3.35.14.95']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}
