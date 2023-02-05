from .models import UserFinance

from rest_framework import serializers


class GetUserFinanceSerializer(serializers.ModelSerializer):
    """
    Filtered display user information
    """

    avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = UserFinance
        exclude = (
            "password",
            "first_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )
