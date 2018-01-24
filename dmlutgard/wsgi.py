import os
import dotenv  # type:ignore

from django.core.wsgi import get_wsgi_application  # type:ignore
from whitenoise.django import DjangoWhiteNoise  # type:ignore


try:
	dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
except UserWarning:
	pass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dmlutgard.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)  # , root='/path/to/static/files')
