# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-12 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0008_entitycomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='comment',
            field=models.IntegerField(default=0),
        ),
    ]