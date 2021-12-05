"""
WSGI application variable using whiskey get application variable 
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_crm.settings')

application = get_wsgi_application()
