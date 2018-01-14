# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-13 14:04
from __future__ import unicode_literals

from django.db import migrations
import videokit.models


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0002_auto_20180113_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediaitem',
            name='video_mp4',
            field=videokit.models.VideoSpecField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='video_ogg',
            field=videokit.models.VideoSpecField(blank=True, null=True, upload_to=b''),
        ),
    ]
