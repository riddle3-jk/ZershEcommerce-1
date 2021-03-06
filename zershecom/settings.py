"""
Django settings for zershecom project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import dj_database_url
import dotenv
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# This is new:
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eq)v7)#87b)+a_^ykuldxo0i7j+x0zpz)c7)iwgu+et7hc%=^)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['dfb-zersh.herokuapp.com', 'zersh.shop', 'www.zersh.shop', '*']


# Application definition

INSTALLED_APPS = [
    # my apps
    'user.apps.UserConfig',
    'store.apps.StoreConfig',
    'pages.apps.PagesConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cloudinary_storage',
    'cloudinary',

    # 3rd party apps
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'djangorave',

    #providors
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zershecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'zershecom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


"""
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
"""    

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

"""    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zershdb',
        'USER': 'zershadmin',
        'PASSWORD': 'admin@zersh',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


AUTH_USER_MODEL = 'user.CustomUser'

#LOGIN_REDIRECT_URL = 'home'
#LOGOUT_REDIRECT_URL = 'home'


# media configurations
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# django-crispy-forms config
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django-allauth config
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'home'

ACCOUNT_SESSION_REMEMBER = True


SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'none'
#ACCOUNT_UNIQUE_EMAIL = True

# email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'zershecommerce@gmail.com'
EMAIL_HOST_PASSWORD = 'z3r5h@dmin'


#djangorave config
"""
RAVE_PRODUCTION_PUBLIC_KEY = "FLWPUBK-17c228ec3029cfd938f1bbc26f25ba19-X"
RAVE_PRODUCTION_SECRET_KEY = "FLWSECK-1e0e2ff19b0db9c09edaa2a6ebe4dd35-X"
RAVE_SANDBOX_PUBLIC_KEY = "FLWPUBK-b79f1bcfe93c4001f53a595c083dee1c-X"
RAVE_SANDBOX_SECRET_KEY = "FLWSECK-b1288e0ffb30b1f8da4dc76f2eb5d23e-X"
RAVE_SANDBOX = True
"""

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

'''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
'''

django_heroku.settings(locals())

options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hgdutrdw7',
    'API_KEY': '457211137331172',
    'API_SECRET': 'QhQ1qfTGt8r0GIUg-YSWgjT3eRA',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

