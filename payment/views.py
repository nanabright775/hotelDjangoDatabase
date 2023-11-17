from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from payment.serializer import PaymentSerializer



class PaymentView(viewsets.ModelViewSet):
    """views for payment"""
    serializer_class = PaymentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



























# import stripe
# from django.shortcuts import render, redirect
# from django.urls import reverse

# stripe.api_key = "sk_test_51O6vrfKHsm9zzL0SEPzUSUD2Pvzs4ghz2WeS8Pt2vSMDtFTIItV4bCHvo8W6LeBjLgSbAbB3WF4aUsoqCIRoTXHr00tfOOBecz"



# def index(request):
# 	return render(request, 'base/index.html')


# def charge(request):
# 	amount = 5
# 	if request.method == 'POST':
# 		print('Data:', request.POST)

# 		Customer = stripe.Customer.createn(
# 			email = request.POST['email'],
# 			name = request.POST['nickname'],
# 			source = request.POST['stripeToken']
# 		)

# 		stripe.Charge.create(
# 			customer = Customer,
# 			amount = 500,
# 			currency = 'usd',
# 			description = 'Donation'
# 		)
  
  
  
# 	return redirect(reverse('success', args=[amount]))
