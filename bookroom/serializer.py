from rest_framework import serializers
from bookroom.models import Room, BookRoom
from user.serializer import UserSerializer


class RoomSerializers(serializers.ModelSerializer):
    """serializers to handle the Rooms"""
    class Meta:
        model = Room
        fields = ['numberofRoom', 'floor_number']
        
        
class BookRoomSerializer(serializers.ModelSerializer):
    """serializers to handle the room bookings"""
    room = RoomSerializers
    user = UserSerializer
    class Meta:
        model = BookRoom
        fields = ['user', 'room', 'check_in_date', 'check_out_date']