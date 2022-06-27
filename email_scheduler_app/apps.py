from django.apps import AppConfig


class EmailSchedulerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_scheduler_app'

    def ready(self):
        from email_updater import updater
        updater.start()
