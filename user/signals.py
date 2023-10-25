from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from user.models import Attendee, User, Manager, Worker
from hotelmanagement import settings

@receiver(post_save, sender = User)
def notify_manager_on_user_creation(sender, instance, created, **kwargs):
    """signal to notify the management that a customer has signed up"""
    if created:
        to_email = instance.email
        send_mail(
            subject = 'Hotel Management Frontdesk',
            message = f'Thank you for choosing our hotel dear:{instance.first_name}',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [to_email],
            fail_silently=True,
        )
 

   
    