"""
Django settings for ShifterAPI project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from configurations import Configuration

class Base(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    LOGIN_URL  = '/admin/login/'
    AUTH_USER_MODEL = "base_app.CustomUser"
    DEFAULT_AUTO_FIELD='django.db.models.AutoField' 
    ALLOWED_HOSTS = ['127.0.0.1:8000']

    # TODO - https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

    INSTALLED_APPS = [
        'django.contrib.admin',         #
        'django.contrib.auth',          #
        'django.contrib.contenttypes',  #
        'django.contrib.sessions',      #
        'django.contrib.messages',      #
        'django.contrib.staticfiles',   #
        'corsheaders',
        'oauth2_provider',
        'rest_framework',
        'base_app',
    ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.middleware.security.SecurityMiddleware',            #
        'django.contrib.sessions.middleware.SessionMiddleware',     #
        'django.middleware.common.CommonMiddleware',                #
        'django.middleware.csrf.CsrfViewMiddleware',                #
        'django.contrib.auth.middleware.AuthenticationMiddleware',  #
        'django.contrib.messages.middleware.MessageMiddleware',     #
        'django.middleware.clickjacking.XFrameOptionsMiddleware',   #
    ]

    ROOT_URLCONF = 'ShifterAPI.urls'

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

    WSGI_APPLICATION = 'ShifterAPI.wsgi.application'


    # Password validation
    # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


    # Internationalization
    # https://docs.djangoproject.com/en/3.1/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.1/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # need to whitelist the url where the frontend is being served.
    #CORS_ORIGIN_WHITELIST = [ 
    #    'https://localhost:3000',
    #]
    # TODO: whitelist instead
    CORS_ORIGIN_ALLOW_ALL = True

    import django_heroku
    django_heroku.settings(locals())

class Dev(Base):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '@r2zg032y4h9zg_z=^wlo868nt4z77s_ps_rr)+rndnc&bu_(y'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'localdb',
            'USER': 'postgres',
            'PASSWORD': 'admin',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

class Prod(Base):
    DEBUG = False

    ALLOWED_HOSTS = ['shifter-backend.herokuapp.com']

    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'railway',
            'USER': 'postgres',
            'PASSWORD': 'OEHKq4LReCNNjg2tQx1f', # TODO: hide in ENV...
            'HOST': 'containers-us-west-153.railway.app',
            'PORT': '7077',
        }
    }