from building import models
from django.views.generic import ListView
from building.serializer import HotelSerializer, HotelDetailSerializer, HotelImageSerializer
from rest_framework import (viewsets, mixins, status)



class HotelView(viewsets.ModelViewSet):
    """viewset for hotel"""
    serializer_class = HotelDetailSerializer
    queryset = models.HotelBuilding.objects.all()
    
    def get_serializer_class(self):
        """return the serializer class for request"""
        if self.action == 'list':
            return HotelSerializer
        elif self.action=='upload_image':
            return HotelImageSerializer
        return self.serializer_class
