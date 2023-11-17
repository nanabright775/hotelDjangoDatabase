from django.urls import (path, include,)
from rest_framework.routers import DefaultRouter
from payment import views

router = DefaultRouter()
router.register('payment', views.PaymentView)

app_name = 'payment'


urlpatterns = [
    path('', include(router.urls)),
]
