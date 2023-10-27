from django.db import models
from django.conf import settings
from django.utils import timezone


class Room(models.Model):
    """models for rooms"""
    guest = models.CharField(max_length=500, blank=True)
    room_number = models.PositiveIntegerField()
    capacity = models.IntegerField()
    floor_number = models.PositiveIntegerField()
    price = models.CharField(max_length=30)
    TYPE = (
        ('executive', 'executive'),
        ('regular', 'regular')
    )
    type = models.CharField(max_length=300, choices=TYPE)
    STATUS = (
        ('free', 'free'),
        ('occupied', 'occupied')
    )
    status = models.CharField(max_length=300, choices=STATUS)

    def __str__(self):
        return f'{self.room_number} {self.type}'
    


class BookRoom(models.Model):
    """modesl for actual room booking"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(default=timezone.now)
    
    
    
      

 
