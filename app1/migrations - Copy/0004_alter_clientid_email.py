# Generated by Django 3.2.12 on 2022-09-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_riskid_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientid',
            name='Email',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
