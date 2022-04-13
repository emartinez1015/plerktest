from django.contrib.auth.models import AbstractUser
from django.db import models
from plerktest.utils.models import PlerkModel


class User(PlerkModel, AbstractUser):
    email = models.EmailField(
        verbose_name="Email Address",
        unique=True,
        error_messages={"unique": "A user with that email already exits"},
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        db_table = "auth_user"
        managed = True
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def get_short_name(self):
        return super().get_short_name()
