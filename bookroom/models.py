from django.db import models
from django.conf import settings
from building.models import HotelBuilding
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import CrontabSchedule,PeriodicTask,ClockedSchedule
from datetime import datetime,timedelta
from django.utils import timezone

# from  . tasks import  schedule_check_out

class Room(models.Model):
    """models for rooms"""
    image = models.ImageField(null=True, upload_to="img/%y")
    numberofRoom = models.PositiveIntegerField()
    floor_number = models.PositiveIntegerField()

    
    
class BookRoom(models.Model):
    """modesl for actual room booking"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(default=timezone.now)   
    book_time_over = models.DurationField(blank=True, null=True)  

    def save(self, *args, **kwargs):
        if self.check_in_date and self.check_out_date:
            self.book_time_over = self.check_out_date - self.check_in_date
        super().save(*args, **kwargs)
    
    
@receiver(post_save, sender=BookRoom)
def send_booking_completion_notification(sender, instance, created, **kwargs):
    
    if instance.check_out_date == "completed":
        from bookroom.tasks import send_notification_task
        send_notification_task.delay(instance.user.email, "Your booking is over.")
