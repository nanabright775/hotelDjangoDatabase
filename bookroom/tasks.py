from user.models import User

from celery import shared_task
from django.core.mail import send_mail
from hotelmanagement import settings
from django.utils import timezone
from datetime import timedelta

@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Hotel Management Frontdesk"
        message = "Please your booking time is over. Thank You"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"