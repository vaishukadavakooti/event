from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Represents the object manager for the user
    """

    def create_user(self, name, email, password=None):
        """
        Create a general user for the system
        :return: user
        """
        if not email:
            raise ValueError("Email address is mandatory")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        """
        Create a super user for the system
        :return: user object
        """

        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents the user profile in our system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_name(self):
        """
        Get the full name of the user
        :return: string
        """
        return self.name

    def get_short_name(self):
        """
        Get the short name of the user
        :return: string
        """
        return self.name

    def __str__(self):
        """
        Represents the model object as string
        :return: string
        """
        return self.email

