from django.db import models

class HotelBuilding(models.Model):
    """model the actual hotel its self"""
    owner_name = models.CharField(max_length=255)
    name = models.CharField(max_length=250)
    address = models.TextField()
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    number_of_floors = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField()
    has_swimming_pool = models.BooleanField(default=False)
    has_fitness_center = models.BooleanField(default=False)
    opening_date = models.DateField()
    last_renovation_date = models.DateField()
    image=models.ImageField(upload_to="img/%y")

    def __str__(self):
         return f"{self.name} ({self.city}, {self.region}, {self.address}, {self.country}, {self.description},)"
