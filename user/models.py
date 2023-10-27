from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password


class User(AbstractUser, PermissionsMixin):
    """Custom user model."""
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, unique=True, null=True)
    Address = models.TextField()
    is_manager = models.BooleanField(default=False)
    is_attendee = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    
    def save(self, *args , **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Manager(models.Model):
    """models for managers"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_manager = True
        user.save()
        super().save(*args, **kwargs)


class Department(models.Model):
    """models for department """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    role = models.CharField(max_length=255)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_worker = True
        user.save()
        super().save(*args, **kwargs)


class Attendee(models.Model):
    """Model for attendees at a hotel."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.user.username)
        user.is_attendee = True
        user.save()
        super().save(*args, **kwargs)
