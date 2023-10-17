from django.db import models
from django.conf import settings
class Room:
    """models for rooms"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    total_number = models.PositiveIntegerField()
    floor_number = models.PositiveIntegerField()
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    