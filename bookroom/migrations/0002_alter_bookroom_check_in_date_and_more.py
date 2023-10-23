# Generated by Django 4.2.6 on 2023-10-19 05:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookroom',
            name='check_in_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='check_out_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]