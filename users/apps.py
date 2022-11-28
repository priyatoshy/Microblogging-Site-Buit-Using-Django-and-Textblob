from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    #letting django know about the signals.py method
    def ready(self):
        import users.signals