
from django.urls import (path, include,)
from rest_framework.routers import DefaultRouter
from bookroom import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
router.register('bookroom', views.BookRoomView)
router.register('room', views.RoomView)

app_name = 'bookroom'


urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
