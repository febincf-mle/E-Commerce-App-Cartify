from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User


class CustomUserManager(BaseUserManager):
    """
    Custom implementation for UserManager, inherits from BaseUserManger and
    overrides the create_user method for the CustomUser Model we created."""
    def create_user(self, email, password=None, **extra_fields):
        """
        Overriden method from BaseUserManager, creates a new user 
        using email field.
        ---
        paramters: 
        - email: str (required)
        - password: str"""
        if not email:
            raise ValueError('The Email field must be set')
        # Normalize the email using the method
        # from the BaseUserManager class.
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Overriden method from BaseUserManager, creates a super user 
        using email field.
        ---
        paramters: 
        - email: str (required)
        - password: str"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
