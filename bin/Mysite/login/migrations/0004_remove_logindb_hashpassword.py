# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_logindb_hashpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logindb',
            name='hashpassword',
        ),
    ]
