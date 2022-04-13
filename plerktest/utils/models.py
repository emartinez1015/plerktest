from django.db import models
from uuid import uuid4 as uuid_generator


class PlerkModel(models.Model):
    id = models.UUIDField(unique=True, default=uuid_generator, primary_key=True)
    created_at = models.DateTimeField(verbose_name="created at",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now_add=True,)

    class Meta:
        abstract = True
        get_latest_by = ["created_at"]
        ordering = ["-created_at", "-updated_at"]
