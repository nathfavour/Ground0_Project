"""This file holds information that will be used
when hosting or deploying this project"""


"""
ASGI config for Ground0_Nathaniel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ground0_Nathaniel.settings')

application = get_asgi_application()
