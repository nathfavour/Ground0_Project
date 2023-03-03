
"""this makes it possible for the project
app to be configured and connected"""

from django.apps import AppConfig


class NathanielConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Nathaniel'
