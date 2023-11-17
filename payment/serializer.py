from rest_framework import serializers
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """serializers for the payment models"""
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method', 'payment_status']