"""
ASGI config for Exp3Backend_CastilloRiquelmeSandoval_006D project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Exp3Backend_CastilloRiquelmeSandoval_006D.settings')

application = get_asgi_application()
