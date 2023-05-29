# Generated by Django 3.2.12 on 2022-11-17 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_basiciddetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='modules_details',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Qn', models.CharField(blank=True, max_length=15, null=True)),
                ('Ans', models.CharField(blank=True, max_length=15, null=True)),
                ('module_name', models.CharField(blank=True, max_length=15, null=True)),
                ('dateandtime', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.basiciddetails')),
            ],
        ),
    ]