from django.apps import AppConfig


class FlagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flag'
    verbose_name = '{{wp-admin}}'
