# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0049_auto_20170819_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='populated',
            field=models.BooleanField(default=False),
        ),
    ]
