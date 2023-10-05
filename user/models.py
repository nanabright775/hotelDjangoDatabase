from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    """abstract user from Django provided user"""
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_attendee = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set2', blank=True)


class Staff(models.Model):
    """staff models"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Address = models.TextField()
    Contact = models.SmallIntegerField()
    role = models.CharField(max_length=255)  # Specify max_length for the role field
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
    name = models.CharField(max_length=255)
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
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
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
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(max_length=15)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room_number = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_attendee = True
        user.save()
        super().save(*args, **kwargs)

    
