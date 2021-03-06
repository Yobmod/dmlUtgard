from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

# class CachedS3BotoStorage(S3BotoStorage):
# 	"""	S3 storage backend that saves the files locally, too."""
# 	def __init__(self, *args, **kwargs):
# 		super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
# 		self.local_storage = get_storage_class(
# 			"compressor.storage.CompressorFileStorage")()
#
# 	def save(self, name, content):
# 		self.local_storage._save(name, content)
# 		super(CachedS3BotoStorage, self).save(name, self.local_storage._open(name))
# 		return name

from storages.backends.s3boto import S3BotoStorage
from compressor.storage import CompressorFileStorage
from django.core.files.storage import get_storage_class
import copy


class CachedS3BotoStorage(S3BotoStorage):
	""" S3 storage backend that saves the files locally, too.  """
	location = settings.STATICFILES_LOCATION

	def __init__(self, *args, **kwargs) -> None:
		super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
		self.local_storage = get_storage_class(
			"compressor.storage.CompressorFileStorage")()

	def url(self, name: str) -> str:
		""" Fix the problem of dont show the natives images django admin"""
		url = super(CachedS3BotoStorage, self).url(name)
		if name.endswith('/') and not url.endswith('/'):
			url += '/'
		return url

	def save(self, name: str, content) -> str:
		content2 = copy.copy(content) #-> THE SECRET IS HERE
		name = super(CachedS3BotoStorage, self).save(name, content)
		self.local_storage._save(name, content2) #-> AND HERE
		# print id(content)
		# print id(content2)
		return name

	def get_available_name(self, name: str, max_length: int) -> str:
		if self.exists(name):
			self.delete(name)
		return name


MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'


class StaticStorage(S3Boto3Storage):
	location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
	location = settings.MEDIAFILES_LOCATION
