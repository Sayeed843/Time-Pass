# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.CharField(default=0, max_length=2000),
            preserve_default=False,
        ),
    ]
