from user.models import User
from bookroom.models import Room
from celery import shared_task
from django.core.mail import send_mail
from hotelmanagement import settings
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(bind=True)
def send_mail_func(self, user_id, room_id):
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
    room = Room.objects.get(id=room_id)
    room.guest = ''
    room.status = 'free'
    room.save()

