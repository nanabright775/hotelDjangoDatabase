from django.contrib import admin
from user import models
# Register your models here.


admin.site.register(models.User)
admin.site.register(models.Worker)
admin.site.register(models.Attendee)
admin.site.register(models.Manager)
admin.site.register(models.Department)
