"""urls for the hotel building"""

from django.urls import (path, include,)
from rest_framework.routers import DefaultRouter
from building import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
router.register('hotelbuilding', views.HotelView)

app_name = 'building'

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
