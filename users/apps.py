from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

#function that imports the signals into the app and we're ready to create and save new profiles without using the admin page
    def ready(self):
        import users.signals
