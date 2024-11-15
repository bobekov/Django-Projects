from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'travel_project.user_profile'

    def ready(self):
        import travel_project.user_profile.signals
