# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 01:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160308_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='last_name',
        ),
    ]
