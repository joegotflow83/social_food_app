# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
