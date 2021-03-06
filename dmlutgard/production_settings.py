import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ["dmlutgard.herokuapp.com"]

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.postgresql_psycopg2',
# 		'NAME': 'dmlutgard',
# 		'USER': 'dmlutgard',
# 		'PASSWORD': '',
# 		'HOST': 'localhost',
# 		'PORT': '',
# 		'CONN_MAX_AGE': 600,
# 	}
# }
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# DATABASES['default'] = dj_database_url.config()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWSAccessKeyId']
AWS_SECRET_ACCESS_KEY = os.environ['AWSSecretKey']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_HOST = 's3.eu-central-1.amazonaws.com'
AWS_IS_GZIPPED = True
# AWS_S3_CUSTOM_DOMAIN = ''
AWS_S3_OBJECT_PARAMETERS = {
	'CacheControl': 'max-age=86000',
}

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'dmlutgard.storages_custom.MediaStorage'


STATICFILES_LOCATION = 'static'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATICFILES_STORAGE = 'dmlutgard.storages_custom.StaticStorage'
STATIC_ROOT = STATICFILES_STORAGE

# STATICFILES_STORAGE ='dmlutgard.storages_custom.CachedS3BotoStorage'.
COMPRESS_STORAGE = STATICFILES_STORAGE
