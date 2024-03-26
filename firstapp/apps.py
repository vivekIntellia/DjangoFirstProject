from django.apps import AppConfig


class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firstapp'


from django.apps import AppConfig

class EducationConfig(AppConfig):
    name = 'education'

    def ready(self):
        from viewflow import registry
        from .flows import EducationFlow
        registry.register(EducationFlow)

