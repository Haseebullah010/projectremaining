# Generated by Django 3.2.16 on 2023-04-11 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_auto_20230411_0505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whatsapp_medical_detail',
            old_name='alcohal',
            new_name='chest_alcohol',
        ),
        migrations.RenameField(
            model_name='whatsapp_medical_detail',
            old_name='asthama',
            new_name='chest_diagnose_Asthma',
        ),
        migrations.RenameField(
            model_name='whatsapp_medical_detail',
            old_name='cholestrol',
            new_name='chest_diagnose_High_Cholesterol',
        ),
        migrations.RenameField(
            model_name='whatsapp_medical_detail',
            old_name='covid',
            new_name='chest_diagnose_Hypertension',
        ),
        migrations.RenameField(
            model_name='whatsapp_medical_detail',
            old_name='diabetes',
            new_name='chest_diagnose_diabetes',
        ),
        migrations.RenameField(
            model_name='whatsapp_medical_detail',
            old_name='hypertension',
            new_name='chest_recent_covid',
        ),
        migrations.RenameField(
            model_name='whatsapp_medical_detail',
            old_name='smoking',
            new_name='chest_smoke',
        ),
        migrations.AlterField(
            model_name='feedbackupdated',
            name='dateandtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 11, 6, 39, 56, 90996)),
        ),
    ]