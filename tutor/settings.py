# -*- coding: utf-8 -*-
"""
Django settings for tutor project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6w%xrgr26r&e^^ovq(vu=67o8=-%fm2g1_!z(30jxkluhubq)p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [

    # sentry
    # 'raven.contrib.django.raven_compat',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third app
    'rest_framework',
    'rest_framework_swagger',
    'gunicorn',

    # my app
    "common",
    "customer",
    "teacher",
    "student",
    "operation"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'common.middleware.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tutor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tutor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('DB_HOST', '114.112.75.135'),
        'NAME': os.environ.get('DB_NAME', 'tutor2'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'P@$$w0rd'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOG_DIR = os.environ.get("LOG_DIR", "logs")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'utils.log_kit.MyLoggerHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'when': 'MONTH', # 1 月
            'backupCount': 12,
            'formatter': 'verbose',
            'encoding': 'UTF-8'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(pathname)s %(lineno)s %(funcName)s %(message)s'
        },
        'short': {
            'format': '%(asctime)s %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['default', 'sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['default', 'sentry'],
            'level': 'INFO',
            'propagate': True,
        },
        'common': {
            'handlers': ['default', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'customer': {
            'handlers': ['default', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'libs': {
            'handlers': ['default', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'student': {
            'handlers': ['default', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'teacher': {
            'handlers': ['default', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'operation': {
            'handlers': ['default', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# rest api setting
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'common.utils.CustomPagination',
    'PAGE_SIZE': 20,
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
}

# token expire time
TOKEN_EXPIRE_TIME = 31536000    # one year