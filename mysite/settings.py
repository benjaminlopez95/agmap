<<<<<<< HEAD
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zj0_rw!ku2qc)bb2zwl$+av@!t$9_((o&u5lsv9aw^1erno-9@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'leaflet',
    'djgeojson',
    'jsonfield',
    'home',
    'plots',
    'view',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mysite.middleware.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite/media')

LOGIN_REDIRECT_URL = '/home/'

LOGIN_URL ='/account/login/'

LOGIN_EXEMPT_URLS = (
    r'^account/logout/$',
    r'^account/register/$',
    r'^account/reset-password/$',
    r'^account/reset-password/done/$',
    r'^account/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    r'^account/reset-password/complete/$'

)

EMAIL_HOST = 'localhost'

EMAIL_PORT = '1025'

LEAFLET_CONFIG = {
    'SPATIAL_EXTENT': (-500, 100, -100, 10),
    'DEFAULT_CENTER': (32.69, -114.63),
    'DEFAULT_ZOOM': 10,
    'MIN_ZOOM': 7,
    'MAX_ZOOM': 19,
    'SCALE': 'imperial',
    'TILES':'https://api.mapbox.com/v4/mapbox.streets-satellite/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYWdtYXBwIiwiYSI6ImNqZXNzaHIyajQycTcyd21lNjNoMGJlazgifQ.HKDOujmAPy7I_mWM40Pl1A',
    'RESET_VIEW': False,
    'PLUGINS': {
        'locate': {
            'js': ['/static/home/locate/locate.js', '/static/home/locate/locate2.js', '/static/home/locate/script.js'],
            'auto-include': True
    },
        'forms': {
            'auto-include': True
        }

    }

}
=======
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zj0_rw!ku2qc)bb2zwl$+av@!t$9_((o&u5lsv9aw^1erno-9@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'leaflet',
    'djgeojson',
    'jsonfield',
    'home',
    'plots',
    'view',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mysite.middleware.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite/media')

LOGIN_REDIRECT_URL = '/home/'

LOGIN_URL ='/account/login/'

LOGIN_EXEMPT_URLS = (
    r'^account/logout/$',
    r'^account/register/$',
    r'^account/reset-password/$',
    r'^account/reset-password/done/$',
    r'^account/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    r'^account/reset-password/complete/$'

)

EMAIL_HOST = 'localhost'

EMAIL_PORT = '1025'

LEAFLET_CONFIG = {
    'SPATIAL_EXTENT': (-500, 100, -100, 10),
    'DEFAULT_CENTER': (32.69, -114.63),
    'DEFAULT_ZOOM': 10,
    'MIN_ZOOM': 7,
    'MAX_ZOOM': 19,
    'SCALE': 'imperial',
    'TILES':'https://api.mapbox.com/v4/mapbox.streets-satellite/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYWdtYXBwIiwiYSI6ImNqZXNzaHIyajQycTcyd21lNjNoMGJlazgifQ.HKDOujmAPy7I_mWM40Pl1A',
    'RESET_VIEW': False,
    'PLUGINS': {
        'locate': {
            'js': ['/static/home/locate/locate.js', '/static/home/locate/locate2.js', '/static/home/locate/script.js'],
            'auto-include': True
    },
        'forms': {
            'auto-include': True
        }

    }

}
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
