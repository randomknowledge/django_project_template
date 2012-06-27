import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir)

_ = lambda s: s

PROJECT_NAME = '{{ project_name }}'
TEMPLATE_DEBUG = True
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de'
SITE_ID = 1

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

USE_I18N = True
USE_L10N = True
USE_TZ = True

EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '0pfue7nasaJd8agsd3123213tghhj3"b)lna4*f_-xxkszs4##!+wpo'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

MIDDLEWARE_CLASSES = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATE_DIRS = (
)
STATICFILES_DIRS = (
    '%s/static' % BASE_DIR,
)
LOCALE_PATHS = (
    '%s/locale' % BASE_DIR,
)

