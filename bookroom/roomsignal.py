from django.db.models.signals import post_save
from django.dispatch import receiver
from bookroom.models import BookRoom
from django_celery_beat.models import PeriodicTask, ClockedSchedule
from hotelmanagement import settings
from django.core.mail import send_mail
# from bookroom.tasks import notify_user_for_bookedroom
import json

@receiver(post_save, sender=BookRoom)
def schedule_checkout(sender, instance, created, **kwargs):
    if created:
        schedule = ClockedSchedule.objects.create(
            clocked_time=instance.check_out_date)
        PeriodicTask.objects.create(
            clocked=schedule, 
            name=f'checkoutMessage{instance.user.id}', 
            task='bookroom.tasks.send_mail_func', 
            one_off=True,
            args=json.dumps((f'{instance.user.id}',))) 


@receiver(post_save, sender=BookRoom)
def send_booking_completion_notification(sender, instance, created, **kwargs):

    if created:
        to_email = instance.user.email
        send_mail(
            subject='Hotel Management Frontdesk',
            message=f'Dear :{instance.user.first_name} your room is booked successfully',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
