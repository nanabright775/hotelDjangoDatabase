from rest_framework import serializers
from user.models import (User, Staff, Worker, Manager,Attendee, Department)
from django.contrib.auth import (
    get_user_model,
    authenticate,
)


class UserSerializer(serializers.ModelSerializer):
    """serializers for model serializers"""
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'is_staff',
            'is_manager',
            'is_attendee',
            'is_worker',
            'groups',
            'user_permissions',
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
    name = UserSerializer
    
    class Meta:
        model = Staff
        fields = ['name', 'Contact',]
    
class StaffDetailSerializer(serializers.ModelSerializer):
    """serializer for the staff detail"""
    name = UserSerializer
    
    class Meta:
        model = Staff
        fields = ['name', 'Address','Contact', 'role', 'staff_id']
        read_only_fields = ['staff_id']
        
class WorkerSerializer(serializers.ModelSerializer):
    """serializers for model worker"""
    name = UserSerializer
    class Meta:
        model = Worker
        fields = ['name', 'Address']
   
   
class ManagerSerializer(serializers.ModelSerializer):
    """serializers for manager"""
    name = UserSerializer
    class Meta:
        model = Manager
        fields = ['name', ]
    
class ManagerDetailSerializer(serializers.ModelSerializer):
    """serializers for manager details"""
    name = UserSerializer
    class Meta:
        model = Manager
        fields = ['name', 'Address', 'Contact']
        read_only_fields = ['id']
   
   
        
class DepartmentSerializer(serializers.ModelSerializer):
    """serializers for department model"""
    manager = ManagerSerializer
    class Meta:
        model = Department
        fields = ['name', 'description', 'manager']
        
class WorkerDetailSerializer(serializers.ModelSerializer):
    """serializers for model worker detail"""
    name = UserSerializer
    department = DepartmentSerializer
    class Meta:
        model = Worker
        fields = ['id','name', 'Address', 'Contact', 'role', 'department']
        read_only_fields = ['id']
        
    
class AttendeeSerializer(serializers.ModelSerializer):
    """serializers for attendees"""
    name = UserSerializer
    class Meta:
        model = Attendee
        fields = ['name', 'phone_number']
    
class AttendeeDetailSerializer(serializers.ModelSerializer):
    """serializers for attendees details"""
    name = UserSerializer
    class Meta:
        model = Attendee
        fields = ['name', 'phone_number', 'check_in_date', 'check_out_date', 'room_number', 'special_requests']
        read_only_fields = ['id']
        
