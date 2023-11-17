from django.db import models
from user.models import User  # You can use your custom user model if applicable
# from bookroom.models import Room


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_checkout_id = models.CharField(max_length=500)
    amount = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    payment_status = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return f"Payment by {self.user.username} - {self.amount} USD ({self.payment_status})"

