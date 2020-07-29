from project.settings.default import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env('DB_NAME'),
        'USER': get_env('TEST_DB_USER'),
        'PASSWORD': get_env('TEST_DB_PASSWORD'),
        'HOST': get_env('TEST_DB_HOST'),
        'PORT': get_env('TEST_DB_PORT'),
    }
}
