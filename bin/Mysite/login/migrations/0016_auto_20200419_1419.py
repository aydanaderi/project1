# Generated by Django 3.0.5 on 2020-04-19 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20200419_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 14, 19, 12, 313587)),
        ),
        migrations.AlterField(
            model_name='information',
            name='profile',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 14, 19, 12, 313612)),
        ),
    ]
