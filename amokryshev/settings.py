import os
import environ
from pathlib import Path
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_PATH = os.path.join(BASE_DIR, '.env')
env = environ.Env()
if os.path.isfile(ENV_PATH):
    environ.Env.read_env(env_file=ENV_PATH)

SECRET_KEY = env('DJ_SECRET_KEY')

DEBUG = env('DJ_DEBUG')
ALLOWED_HOSTS = env.list('DJ_ALLOWED_HOSTS')

THREAD_SERVER_HOST = '127.0.0.1'
THREAD_SERVER_PORT = 8290

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'webpack_loader',
    'mainsite',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'amokryshev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.i18n',
                #'django.template.context_processors.media',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'mainsite.context_processors.load_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'amokryshev.wsgi.application'

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DJ_DEFAULT_DB_NAME'),
        'USER': env('DJ_DEFAULT_DB_USER'),
        'PASSWORD': env('DJ_DEFAULT_DB_PASS'),
        'HOST': env('DJ_DEFAULT_DB_HOST'),
        'PORT': env('DJ_DEFAULT_DB_PORT'),

    },
    'adm': {

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DJ_ADM_DB_NAME'),
        'USER': env('DJ_ADM_DB_USER'),
        'PASSWORD': env('DJ_ADM_DB_PASS'),
        'HOST': env('DJ_ADM_DB_HOST'),
        'PORT': env('DJ_ADM_DB_PORT'),

        }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION":  env('DJ_CACHE_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX":  env('DJ_CACHE_PREFIX')
    }
}

CACHE_TIMEOUT = env.int('DJ_CACHE_TIMEOUT')

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
     },
     'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
         }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
]

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'node_modules/bootstrap/'),
    os.path.join(BASE_DIR, 'node_modules/jquery/'),
    os.path.join(BASE_DIR, 'node_modules/jquery-ui/'),
    os.path.join(BASE_DIR, 'node_modules/popper.js/'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'static/bundles/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

SUMMERNOTE_CONFIG = { 'iframe': False, }
