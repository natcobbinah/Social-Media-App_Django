from django.apps import AppConfig


class BookmarkImagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bookmark_images"

    def ready(self):
        # import signal handlers
        import bookmark_images.signals
