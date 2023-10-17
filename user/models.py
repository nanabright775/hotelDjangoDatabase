from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Custom user manager for a Django custom user model."""

    def create_user(self, first_name, last_name, username, email, password=None):
        """Function for creating a regular user."""
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        """Function for creating a superuser."""
        user = self.create_user(
            email=self.normalize_email(email),  # Fixed typo: 'rais' to 'raise'
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password  # Added the missing comma after 'last_name'
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_attendee = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='customuser_set2', blank=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Staff(models.Model):
    """staff models"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Address = models.TextField()
    Contact = models.SmallIntegerField()
    role = models.CharField(max_length=255)
    staff_id = models.SmallIntegerField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_staff = True
        user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Staff ID: {self.staff_id:08d}"


class Manager(models.Model):
    """models for managers"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Address = models.TextField()
    Contact = models.SmallIntegerField()

    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_staff = True
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
    phone_number = models.CharField(max_length=15)
    Address = models.TextField()
    Contact = models.SmallIntegerField()
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
    phone_number = models.CharField(max_length=15)
    special_requests = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.user.username)
        user.is_attendee = True
        user.save()
        super().save(*args, **kwargs)
