# Generated by Django 3.0.5 on 2020-04-19 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20200419_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.BigIntegerField()),
                ('password', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 4, 19, 13, 55, 56, 923125))),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 4, 19, 13, 55, 56, 923148))),
                ('email', models.EmailField(max_length=254)),
                ('profile', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
        migrations.DeleteModel(
            name='Logindb',
        ),
    ]
