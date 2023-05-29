# Generated by Django 3.2.12 on 2022-11-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_disease_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicIdDetails',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Unique_ID', models.CharField(blank=True, max_length=15)),
                ('DOB', models.CharField(blank=True, max_length=15)),
                ('Age', models.CharField(blank=True, max_length=15)),
                ('Sex', models.CharField(blank=True, max_length=15)),
                ('Height', models.CharField(blank=True, max_length=5)),
                ('Weight', models.CharField(blank=True, max_length=15)),
                ('BMI', models.CharField(blank=True, max_length=15)),
                ('Smoker', models.CharField(blank=True, max_length=15)),
                ('alcohal', models.CharField(blank=True, max_length=15)),
                ('phonenumber', models.CharField(blank=True, max_length=50)),
                ('Email', models.CharField(blank=True, max_length=150)),
                ('Covid', models.CharField(blank=True, max_length=15)),
                ('Suffering_Duration', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
