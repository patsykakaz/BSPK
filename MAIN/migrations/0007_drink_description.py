# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0006_home_baseline'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='description',
            field=models.TextField(default=False),
        ),
    ]
