from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from user.models import Attendee, Worker

@receiver(post_save, sender = Attendee)
def notify_manager_on_user_creation(sender, instance, created, **kwargs):
    """signal to notify the management that a customer has signed up"""
    if created:
        subject = 'New User Created'
        message = f'A new user has been added with the booker:{instance.user}'
        from_email = 'your_email@example.com'
        recipient_list = ['manager@example.com']  # Replace with the manager's email address
        send_mail(subject, message, from_email, recipient_list)
    
    
@receiver(post_save, sender = Worker)
def notify_manager_on_user_creation(sender, instance, created, **kwargs):
    """signal to notify the manger that a new worker has been added"""
    if created:
        subject = 'New worker Created'
        message = f'A new worker has been added with the username: {instance.username}, email: {instance.email} and phone number: {instance.phone_number} and department: {instance.department}.'
        from_email = 'your_email@example.com'
        recipient_list = ['manager@example.com']  # Replace with the manager's email address
        send_mail(subject, message, from_email, recipient_list)