from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth'
    label = 'Aauth'

    def ready(self):
        import auth.signals  # noqa
