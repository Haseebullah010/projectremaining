# Generated by Django 3.2.16 on 2023-05-12 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0036_auto_20230512_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentdatanew',
            name='fromwhichsite',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackupdated',
            name='dateandtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 12, 6, 41, 20, 51972)),
        ),
    ]
