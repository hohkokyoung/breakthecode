from django.apps import AppConfig
from injector import Binder, Injector
from .injectors import ChallengeModule

class ChallengesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'challenges'

    def ready(self):
        injector = Injector()
        binder = Binder(injector)
        binder.install(ChallengeModule)
