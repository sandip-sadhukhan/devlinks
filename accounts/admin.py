from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.utils.translation import gettext_lazy as _

class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        fields = ("username", "email",)


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

admin.site.register(User, UserAdmin)

