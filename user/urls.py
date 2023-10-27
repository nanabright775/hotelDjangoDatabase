"""
urls mapping for the hotell users app
"""

from django.urls import (
    path,
    include,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register('manager', views.ManagerView, basename='manager')
router.register('worker', views.WorkerVIew, basename='worker')
router.register('department', views.DepartmentView, basename='department')
router.register('attendee', views.AttendeeView)


app_name = 'user'

urlpatterns = [
    path('', include(router.urls)),
    path('create/user/', views.CreateUserView.as_view(), name='create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', views.ManageUserView.as_view(), name='me')
]