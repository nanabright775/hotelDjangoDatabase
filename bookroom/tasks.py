from user.models import User
from bookroom.models import BookRoom, Room
from datetime import datetime
from celery import shared_task
from django.core.mail import send_mail
from hotelmanagement import settings
from celery.utils.log import get_task_logger
from django_celery_beat.models import PeriodicTask, CrontabSchedule
    
logger = get_task_logger(__name__)

@shared_task(bind=True)
def send_mail_func(self, data):
    user_id = data
    user = User.objects.get(id=user_id)
    mail_subject = "Hotel Management Frontdesk"
    message = f"Dear {user.first_name}, your booking time is over. Thank You"
    to_email = user.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )

    Room.status = 'free'
    Room.guest = ''
        

    # return "Done"

# @shared_task(bind=True)
# def notify_user_for_bookedroom(self):
#     to_email = BookRoom.user.email
#     send_mail(
#         subject='Hotel Management Frontdesk',
#         message=f'Dear :{BookRoom.user.first_name} your room is booked successfully',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[to_email],
#         fail_silently=True,
#     )
    # return "Done"