from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import UserFinance, Settings

from django.utils.translation import gettext, gettext_lazy as _


class UserFinanceAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone",
        "first_login",
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": ("is_active",),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Info"), {"fields": ("phone", "avatar", "gender")}),
    )


admin.site.register(UserFinance, UserFinanceAdmin)
admin.site.register(Settings)
