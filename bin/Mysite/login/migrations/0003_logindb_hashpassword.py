# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200405_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindb',
            name='hashpassword',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
