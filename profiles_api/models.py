from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(
        self,
        email,
        name,
        phone_number,
        tester="default tester",
        password=None,
        is_active=True,
        is_black=False,
    ):  # This is ALL of the data of a user.
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone_number=phone_number,
            tester=tester,
            is_active=is_active,
            is_black=is_black,
        )

        user.set_password(password)
        # This is required to save the user to the database
        # The password is hashed by the set_password method,
        #  so we need to save the user to the database to store the hashed password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    tester = models.CharField(max_length=255, default="Forced Text")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_black = models.BooleanField(default=False)
    objects = UserProfileManager()
    # Note that the password field is not explicitly defined in the UserProfile model because it is inherited from the AbstractBaseUser class. The AbstractBaseUser class provides a password field and methods for handling password hashing and authentication, so we don't need to define it ourselves in the UserProfile model. By inheriting from AbstractBaseUser, we can take advantage of the built-in functionality for managing user authentication and password handling without having to implement it ourselves.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
