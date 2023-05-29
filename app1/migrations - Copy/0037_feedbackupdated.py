# Generated by Django 3.2.16 on 2022-12-27 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0036_id_dec_dateandtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackupdated',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('senderid', models.CharField(blank=True, max_length=150)),
                ('DiagnosticAccuracy', models.CharField(blank=True, max_length=15)),
                ('UserExperience', models.CharField(blank=True, max_length=15)),
                ('Likelihoodtorecommend', models.CharField(blank=True, max_length=15)),
                ('dateandtime', models.DateTimeField(default=datetime.datetime(2022, 12, 27, 7, 21, 52, 392187))),
            ],
        ),
    ]
