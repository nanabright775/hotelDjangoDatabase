import os
from celery import Celery
from datetime import timedelta
# from bookroom.models import BookRoom


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotelmanagement.settings')
app = Celery('hotelmanagement')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'UTC'

# app.conf.beat_schedule = {
#     "add_first": {
#         "task": "bookroom.tasks.send_mail_func",
#         "schedule": timedelta(days=1),
#     },
# }

app.autodiscover_tasks()
