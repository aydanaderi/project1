# Generated by Django 3.0.5 on 2020-04-20 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_auto_20200420_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 14, 12, 10, 679519)),
        ),
        migrations.AlterField(
            model_name='information',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 14, 12, 10, 679544)),
        ),
    ]
