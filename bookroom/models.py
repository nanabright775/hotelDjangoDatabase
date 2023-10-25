from django.db import models
from django.conf import settings
from building.models import HotelBuilding
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import CrontabSchedule, PeriodicTask, ClockedSchedule
from datetime import datetime, timedelta
from django.utils import timezone
from user.models import User
# from  . tasks import  schedule_check_out


class Room(models.Model):
    """models for rooms"""
    # image = models.ImageField(null=True, upload_to="img/%y")
    guest = models.CharField(max_length=500, blank=True)
    numberofRoom = models.PositiveIntegerField()
    capacity = models.IntegerField()
    floor_number = models.PositiveIntegerField()
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
        return f'{self.numberofRoom} {self.type}'


class BookRoom(models.Model):
    """modesl for actual room booking"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(default=timezone.now)
    # book_time_over = models.DurationField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if self.check_in_date and self.check_out_date:
    #         schedule = ClockedSchedule.objects.create(
    #             clocked_time=self.check_out_date)
    #         PeriodicTask.objects.create(
    #             clocked=schedule, name=f'task{self.id}', task='bookroom.tasks.send_mail_func', one_off=True)
    #         # self.book_time_over = self.check_out_date - self.check_in_date
    #     super().save(*args, **kwargs)


