import os
from pickle import TRUE
import environ
import dj_database_url
env = environ.Env()

# Leer el archivo .env
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Prodciion en render
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')


#Ambeinte de preuba
#SECRET_KEY = env('SECRET_KEY')
DEBUG = 'RENDER' not in os.environ
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

#

ALLOWED_HOSTS = []
#hostaname de render
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER = 'alfredoji300@gmail.com'
EMAIL_HOST_PASSWORD = env('GMAIL_PASWORD')
EMAIL_USE_TLS = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'core',
    'cart',
    'rest_framework',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #
]

DEFAULT_FROM_EMAIL=env('DEFAULT_FROM_EMAIL')
NOTIFY_EMAIL=env('NOTIFY_EMAIL')
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR),'templates'],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'OPTIONS': {
                'options': '-c search_path=django,public'
            },
            'NAME': 'restaurante',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',

        },
    }


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

SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]
#configuracion de allauth para seguridad en el sistema
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PRESERVE_USERNAME_CASING =True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Verificacion'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
CRISPY_TEMPLATE_PACK='bootstrap4'
LOGIN_REDIRECT_URL='/'

LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_L10N = True



#Cpaypal
PAYPAL_CLIENT_ID=env('PAYPAL_SANDBOX_CLIENT_ID')
PAYPAL_SECRET_KET=env('PAYPAL_SANDBOX_SECRET_KEY')



#arichivos estaticos

STATIC_URL = '/static/'

STATIC_URL = '/static/'
STATICFILES_DIRS =[os.path.join(BASE_DIR,"static")]
STATIC_ROOT = os.path.join(BASE_DIR,"static_root")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


MEDIA_URL = '/media/'
'''

if DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = os.path.join(BASE_DIR, '')
    MEDIA_URL = os.path.join(BASE_DIR, 'media')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    #STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

'''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/




#segurida en el cierre de sesion
SESSION_COOKIE_AGE = 60 * 60 #Tiempo de vida de la sesión en segundos -> x Minutos x 60segundos.  (60min*60seg)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True #Si sale del navegador, cerrar sesión
SESSION_SAVE_EVERY_REQUEST = True  # actualizar tiempo de vida en cada request




if DEBUG is False:

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    #SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    ####
    EMAIL_HOST= 'smtp.gmail.com'
    EMAIL_PORT= 587
    EMAIL_HOST_USER = 'alfredoji300@gmail.com'
    EMAIL_HOST_PASSWORD = env('GMAIL_PASWORD')
    EMAIL_USE_TLS = True
    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases
    #configuracion para render
    DATABASES = {
        'default': dj_database_url.config(
            default='postgresql://postgres:postgres@localhost:5432/postgres',
            conn_max_age=600
        )}

