from ninja import Schema, ModelSchema

from .models import UserFinance


class UserFinancePublicSchema(ModelSchema):
    class Config:
        model = UserFinance
        model_exclude = (
            "email",
            "phone",
            "password",
            "first_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


class UserFinancePrivateSchema(ModelSchema):
    class Config:
        model = UserFinance
        model_exclude = (
            "password",
            "first_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )
