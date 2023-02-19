from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.db import models


class UserFinance(AbstractUser):
    """User model"""

    GENDER = (
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    )

    first_login = models.DateTimeField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GENDER, default="Unknown")

    phone = models.CharField(max_length=14)

    work_place = models.CharField(max_length=150, blank=True, null=True)
    work_position = models.CharField(max_length=150, blank=True, null=True)

    avatar = models.ImageField(
        upload_to="user/avatar/", default="default/default_av.png"
    )


class Settings(models.Model):
    """Settings model for each user"""

    CURRENCY = (
        ("usd", "usd"),
        ("eur", "eur"),
        ("uah", "uah"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_settings"
    )
    currency = models.CharField(max_length=7, choices=CURRENCY, default="usd")

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
