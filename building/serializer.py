from rest_framework import serializers

from building.models import HotelBuilding

class HotelSerializer(serializers.ModelSerializer):
    """serializer for the building"""
    class Meta:
        model = HotelBuilding
        fields = ['name', 'address', 'city', 'region', 'country', 'description',]
        
        
class HotelDetailSerializer(serializers.ModelSerializer):
    """serializer for the building"""
    class Meta:
        model = HotelBuilding
        fields = ['owner_name', 'name', 'address', 'city', 'region', 'country', 'description', 'postal_code', 'number_of_floors', 'number_of_rooms', 'has_swimming_pool', 'has_fitness_center', 'opening_date', 'last_renovation_date']

class HotelImageSerializer(serializers.ModelSerializer):
    """serializer for uploading student images"""
    class Meta:
        model = HotelBuilding
        fields =['image', ]
        read_only_fields=['id']
        extra_kwargs = {'image': {'required': 'True'}}       