# Generated by Django 3.2.16 on 2023-05-25 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0038_auto_20230512_0752'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AppointmentData',
        ),
        migrations.RemoveField(
            model_name='bmidata',
            name='user',
        ),
        migrations.DeleteModel(
            name='Diet_Image',
        ),
        migrations.DeleteModel(
            name='feedbackupdated',
        ),
        migrations.DeleteModel(
            name='ID_Dec',
        ),
        migrations.DeleteModel(
            name='Medibot_Diagnosis_Dec',
        ),
        migrations.DeleteModel(
            name='Medibot_modules_details',
        ),
        migrations.RemoveField(
            model_name='personaldetail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Skin_Image',
        ),
        migrations.DeleteModel(
            name='SurgeryDta',
        ),
        migrations.RemoveField(
            model_name='whatsapp_medical_detail',
            name='user',
        ),
        migrations.DeleteModel(
            name='BMIData',
        ),
        migrations.DeleteModel(
            name='personaldetail',
        ),
        migrations.DeleteModel(
            name='whatsapp_medical_detail',
        ),
    ]
