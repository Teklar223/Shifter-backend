"""
WSGI config for ShifterAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
from ShifterAPI import utils

utils.setConfig()
# from django.core.wsgi import get_wsgi_application

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
