"""
user view for the user api
"""


from user.models import ( Worker, Manager, Department, Attendee, User)
from rest_framework import viewsets
from rest_framework import generics, authentication, permissions
from user.serializer import (UserSerializer,
                             WorkerSerializer, ManagerSerializer, ManagerDetailSerializer, DepartmentSerializer,
                             WorkerDetailSerializer, AttendeeSerializer, AttendeeDetailSerializer)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 


class ManageUserView(generics.RetrieveUpdateAPIView):
    """manage authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """retrieve and return authenticated user"""
        return self.request.user





class WorkerVIew(viewsets.ModelViewSet):
    """views for model views"""
    serializer_class = WorkerDetailSerializer
    queryset = Worker.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ManagerView(viewsets.ModelViewSet):
    """viewset for manager"""
    serializer_class = ManagerDetailSerializer
    queryset = Manager.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ManagerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class DepartmentView(viewsets.ModelViewSet):
    """viewset for model department"""
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AttendeeView(viewsets.ModelViewSet):
    """views for the attendee the person who will purchase the room"""
    serializer_class = AttendeeDetailSerializer
    queryset = Attendee.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AttendeeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
