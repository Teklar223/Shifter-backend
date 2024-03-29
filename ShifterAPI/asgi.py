"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

from ShifterAPI import utils
utils.setConfig()

from configurations.asgi import get_asgi_application
application = get_asgi_application()
