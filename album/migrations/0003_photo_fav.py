# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 13:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0002_auto_20170630_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='fav',
            field=models.ManyToManyField(related_name='fav', to=settings.AUTH_USER_MODEL),
        ),
    ]
