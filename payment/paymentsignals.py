from django.dispatch import receiver
from django.db.models.signals import post_save
from payment.models import Payment
from bookroom.models import BookRoom

@receiver(post_save, sender = BookRoom)
def create_user_payment(sender, instance, created, **kwargs):
    if created:
        Payment.objects.create(user=instance.user, amount=instance.room.price)
        

# @receiver(post_save, sender=Payment)
# def update_payment_status(sender, instance, **kwargs):
#     if instance.stripe_checkout_id and instance.payment_method:
#         instance.payment_status = True
#         print("save")
#         instance.save












     
# @receiver(post_save, sender=BookRoom)
# def create_user_payment(sender, instance, created, **kwargs):
#     if created:
#         user_instance = instance.user
#         room_instance = instance.room  # Assuming your BookRoom model has a ForeignKey field named 'room'
#         payment = Payment.objects.create(user=user_instance, amount=room_instance.price)
 
 