# Generated by Django 4.2.6 on 2023-11-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_status',
        ),
    ]
