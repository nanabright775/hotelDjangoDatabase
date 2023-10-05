"""
urls mapping for the hotell users app
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register('manager', views.ManagerView, basename='manager')
router.register('staff', views.StaffView, basename='staff')
router.register('worker', views.WorkerVIew, basename='worker')
router.register('department', views.DepartmentView, basename='department')
router.register('attendee', views.AttendeeView)



app_name = 'user'

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]