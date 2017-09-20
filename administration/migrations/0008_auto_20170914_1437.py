# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20170912_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='intended_return_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(default='student', max_length=10),
        ),
    ]
