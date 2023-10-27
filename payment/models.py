from django.db import models
from user.models import User  # You can use your custom user model if applicable

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link payment to a user
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Payment by {self.user.username} - {self.amount} USD ({self.payment_status})"

