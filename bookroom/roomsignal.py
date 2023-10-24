from django.db.models.signals import post_save
from django.dispatch import receiver
from bookroom.models import BookRoom
from django_celery_beat.models import CrontabSchedule, PeriodicTask, ClockedSchedule


@receiver(post_save, sender=BookRoom)
def schedule_checkout(sender, instance, created, **kwargs):
    if created:
        schedule = ClockedSchedule.objects.create(
            clocked_time=instance.check_out_date)
        PeriodicTask.objects.create(
            clocked=schedule, name=f'task{instance.id}', task='bookroom.tasks.send_mail_func', one_off=True)
