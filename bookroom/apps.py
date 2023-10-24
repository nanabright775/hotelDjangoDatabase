from django.apps import AppConfig


class BookroomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookroom'
    
    def ready(self):
        import bookroom.roomsignal
