from bookroom.models import Room, BookRoom
from bookroom.serializer import BookRoomSerializer, RoomSerializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BookRoomView(viewsets.ModelViewSet):
    """views for booking room """
    serializer_class = BookRoomSerializer
    queryset = BookRoom.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializers
    queryset = Room.objects.filter(status='free')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
