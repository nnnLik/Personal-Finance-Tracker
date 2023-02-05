from django.contrib.auth.models import AbstractUser
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

    avatar = models.ImageField(upload_to="user/avatar/", blank=True, null=True)
