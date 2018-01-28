import os
import dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	# 'whitenoise.runserver_nostatic',
	'django.contrib.staticfiles',

	'django_extensions',
	'rest_framework',
	'storages',
	# 'channels',
	'compressor',
	# 'sekizai',

	'main',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	# 'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'dmlutgard.urls'
WSGI_APPLICATION = 'dmlutgard.wsgi.application'

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
				"django.template.context_processors.i18n",
				"django.template.context_processors.media",
				'sekizai.context_processors.sekizai',
			],
		},
	},
]

CACHES = {
	'default': {
		# 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		# 'django.core.cache.backends.memcached.MemcachedCache',
		# 'django.core.cache.backends.memcached.PyLibMCCache',
		# 'LOCATION': '/var/tmp/django_cache',
	}
}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
		'rest_framework.renderers.BrowsableAPIRenderer',
	),
	# 'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser', ),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		# 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
		'rest_framework.authentication.SessionAuthentication',
		# 'rest_framework.authentication.BasicAuthentication',
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.AllowAny',  # all views will be this unless has permission class added
		# 'rest_framework.permissions.IsAuthenticated',
		# 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
	)
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
	('text/x-scss', 'django_libsass.SassCompiler'),
)
LIBSASS_OUTPUT_STYLE = 'nested'  # 'compressed'
LIBSASS_PRECISION = 8  # for bootstrap?
# background: url(static("myapp/image/bar.png"));


COMPRESS_CSS_FILTERS = [
	'compressor.filters.css_default.CssAbsoluteFilter',
	'compressor.filters.cssmin.rCSSMinFilter'  # default
]
COMPRESS_JS_FILTERS = [
	'compressor.filters.jsmin.JSMinFilter',  # default
]

# ------------------------------------------------------

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "dmlutgard", "static_cdn")

SITE_ID = 1
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

try:
	dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
except UserWarning:
	pass

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ""  # use in view if different from host

LOCAL = os.environ['LOCAL']
SECRET_KEY = os.environ['SECRET_KEY']


if LOCAL == 'yes':
	DEBUG = True
	print(" * using local environment settings")
	MEDIA_URL = "/media/"
	STATIC_URL = '/static/'
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}
else:
	try:
		from .production_settings import *
		print(" * using production environment settings")
	except ImportError:
		print(" * production environment settings not found")

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = False
# WHITENOISE_AUTOREFRESH # =DEBUG
# WHITENOISE_ROOT = STATIC_ROOT
