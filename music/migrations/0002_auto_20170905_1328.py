# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 04:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_loge',
            new_name='album_logo',
        ),
    ]
