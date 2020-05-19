import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv(os.path.join(settings.BASE_DIR, '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_main.settings')

application = get_wsgi_application()
