from rest_framework import serializers
from user.models import (User, Staff, Worker, Manager,Attendee, Department)
from django.contrib.auth import (
    authenticate,
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
            'groups',
            'user_permissions',
            'password',
        ]
        read_only_fields = ['id']
        
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = ('Unable to authenticate with the provided credentials')
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs
    
class StaffSerializer(serializers.ModelSerializer):
    """serializer for the staff"""
    user = UserSerializer
    
    class Meta:
        model = Staff
        fields = ['user', 'Contact',]
    
class StaffDetailSerializer(serializers.ModelSerializer):
    """serializer for the staff detail"""
    user = UserSerializer
    
    class Meta:
        model = Staff
        fields = ['user', 'Address', 'Contact', 'role', 'staff_id']
        read_only_fields = ['staff_id']
        
class WorkerSerializer(serializers.ModelSerializer):
    """serializers for model worker"""
    user = UserSerializer
    class Meta:
        model = Worker
        fields = ['user', 'Address']
   
   
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
        fields = ['id', 'user', 'Address', 'Contact']
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
        fields = ['id','user', 'Address', 'Contact', 'role', 'department']
        read_only_fields = ['id']
        
    
class AttendeeSerializer(serializers.ModelSerializer):
    """serializers for attendees"""
    user = UserSerializer
    class Meta:
        model = Attendee
        fields = ['user', 'phone_number']
    
class AttendeeDetailSerializer(serializers.ModelSerializer):
    """serializers for attendees details"""
    user = UserSerializer
    class Meta:
        model = Attendee
        fields = [ 'id', 'user', 'special_requests', 'phone_number']
        read_only_fields = ['id']
        
