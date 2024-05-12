from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)

        if not email:
            raise ValueError("Email is required")

        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, blank=False,
                              null=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()
