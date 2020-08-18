from project.settings.default import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('TEST_DB_USER'),
        'PASSWORD': os.getenv('TEST_DB_PASSWORD'),
        'HOST': os.getenv('TEST_DB_HOST'),
        'PORT': os.getenv('TEST_DB_PORT'),
    }
}
