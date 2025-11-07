import os
os.environ['DEBUG'] = 'True'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_portfolio_site.settings')
import django
django.setup()
from django.conf import settings
print('DEBUG:', settings.DEBUG)
print('SECURE_SSL_REDIRECT:', getattr(settings, 'SECURE_SSL_REDIRECT', 'Not set'))
