import os
import dotenv

from django.core.wsgi import get_wsgi_application

try:
	dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
except UserWarning:
	pass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dmlutgard.settings")

application = get_wsgi_application()
