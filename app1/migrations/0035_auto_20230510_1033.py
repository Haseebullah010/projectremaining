# Generated by Django 3.2.16 on 2023-05-10 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_auto_20230510_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentdatanew',
            name='fromwhichapplication',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackupdated',
            name='dateandtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 10, 10, 33, 1, 318161)),
        ),
    ]