from rest_framework import serializers
from user.models import (User, 
                        Worker, Manager,Attendee, Department
                         )


class UserSerializer(serializers.ModelSerializer):
    """serializers for model serializers"""
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'is_active',
            'is_staff',
            'is_manager',
            'is_attendee',
            'is_worker',
            'password',
        ]
        read_only_fields = ['id']
        
class WorkerSerializer(serializers.ModelSerializer):
    """serializers for model worker"""
    user = UserSerializer
    class Meta:
        model = Worker
        fields = ['user']
   
   
class ManagerSerializer(serializers.ModelSerializer):
    """serializers for manager"""
    user = UserSerializer
    class Meta:
        model = Manager
        fields = ['user']
    
class ManagerDetailSerializer(serializers.ModelSerializer):
    """serializers for manager details"""
    user = UserSerializer
    class Meta:
        model = Manager
        fields = ['id', 'user']
        read_only_fields = ['id']
   
   
        
class DepartmentSerializer(serializers.ModelSerializer):
    """serializers for department model"""
    manager = ManagerSerializer
    class Meta:
        model = Department
        fields = ['name', 'description', 'manager']
        
class WorkerDetailSerializer(serializers.ModelSerializer):
    """serializers for model worker detail"""
    user = UserSerializer
    department = DepartmentSerializer
    class Meta:
        model = Worker
        fields = ['id','user', 'role', 'department']
        read_only_fields = ['id']
        
    
class AttendeeSerializer(serializers.ModelSerializer):
    """serializers for attendees"""
    user = UserSerializer
    class Meta:
        model = Attendee
        fields = ['user',]
    
class AttendeeDetailSerializer(serializers.ModelSerializer):
    """serializers for attendees details"""
    user = UserSerializer
    class Meta:
        model = Attendee
        fields = [ 'id', 'user']
        read_only_fields = ['id']
        
