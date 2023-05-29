# Generated by Django 3.2.12 on 2022-11-15 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_auto_20221103_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='disease_details',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('disease', models.CharField(blank=True, max_length=15, null=True)),
                ('module_name', models.CharField(blank=True, max_length=15, null=True)),
                ('dateandtime', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.basic')),
            ],
        ),
    ]
