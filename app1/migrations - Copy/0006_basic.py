# Generated by Django 3.2.12 on 2022-10-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_clientid_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('DOB', models.CharField(blank=True, max_length=15)),
                ('Age', models.CharField(blank=True, max_length=15)),
                ('Sex', models.CharField(blank=True, max_length=15)),
                ('Height', models.CharField(blank=True, max_length=5)),
                ('Weight', models.CharField(blank=True, max_length=15)),
                ('BMI', models.CharField(blank=True, max_length=15)),
                ('Smoker', models.CharField(blank=True, max_length=15)),
                ('Medication', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
