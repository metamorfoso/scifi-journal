import os
from functools import partial
import raven

# ############################ Journal Settings ############################# #
TAKING_SUBMISSIONS = True
PREPARING_NEXT_ISSUE = True

# ########################### Application Settings ########################## #

SRC_ROOT = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(SRC_ROOT, '..', '..', '..'))
project_path = partial(os.path.join, PROJECT_ROOT)

DEBUG = False

ADMINS = (
    ('admin', 'ivanign04@gmail.com'),
)
INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ('52.62.2.21', 'sponge.nz', 'www.sponge.nz',)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sponge',
        'USER': 'spongeuser',
        'PASSWORD': 'SpongeCake???',
        'HOST': 'localhost',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'miracle-yeah.2foko5.cfg.apse2.cache.amazonaws.com:11211',
        'KEY_PREFIX': 'SPONGE'
    }
}

# Change this to cached_db if using memcached
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
TIME_ZONE = 'Pacific/Auckland'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = project_path('media')
UPLOAD_PATH = "uploads/%Y_%m"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = project_path('static')

# URL prefix for static files.
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    project_path("resources"),
)

WHITENOISE_ALLOW_ALL_ORIGINS = True

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Make this unique, and don't share it with anybody.
SECRET_KEY = u"c4#896yo)_ig)^3rt4)!&%m143ei6i%kj1=tc9l*viz31jf#*)"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [project_path('templates')],
        # will look in "jinja2" dir, so doesn't mess with the admin
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'project.jinja_env.environment',
            'extensions': ['pipeline.jinja2.PipelineExtension']
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [project_path('templates/django')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'utilities.middleware.trailing_slash.AppendOrRemoveSlashMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Libraries
    'sorl.thumbnail',
    'raven.contrib.django.raven_compat',
    'memoize',
    'pipeline',
    'num2words',

    # Our apps
    'journal',
    'submissions',
    'subscription'
)

# RAVEN_CONFIG = {
#     'dsn': 'https://59b9e80fd2e649b2ae0caca8184fd1f1'
#            ':83a89849ccb74925a84c20dbf6e2d375@app.getsentry.com/73528',
#     # If you are using git, you can also automatically configure the
#     # release based on the git info.
#     'release': raven.fetch_git_sha(PROJECT_ROOT),
# }

APPEND_SLASH = False  # see AppendOrRemoveSlashMiddleware

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'marbonbros'
EMAIL_HOST_PASSWORD = 'b3t_t3rlat3_thann3v3r'
DEFAULT_FROM_EMAIL = 'system@marbonbros.com'
SERVER_EMAIL = 'system@marbonbros.com'
EMAIL_SUBJECT_PREFIX = "[sponge] "

PIPELINE = dict(
    STYLESHEETS={
        'site': {
            'source_filenames': (
                'c/application.sass',
            ),
            'output_filename': 'style/app.css',

            'extra_context': {
                'media': 'screen,projection,print',
            },
        }
    },
    JAVASCRIPT={
        'app': {
            'source_filenames': (
                'j/lib/modernizr-mq.js',
                'j/lib/jquery.js',
                'j/lib/raven.js',
                'j/lib/slick.js',
                'j/site.js',
            ),
            'output_filename': 'j/app.js'
        }
    },
    COMPILERS=('pipeline.compilers.sass.SASSCompiler',),
    CSS_COMPRESSOR='pipeline.compressors.cssmin.CSSMinCompressor',
    JS_COMPRESSOR='pipeline.compressors.uglifyjs.UglifyJSCompressor'
)

PIPELINE['SASS_BINARY'] = '/usr/local/bin/sass'

STATICFILES_STORAGE = 'project.staticfiles_storage.GzipManifestPipelineStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
