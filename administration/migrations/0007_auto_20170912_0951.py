# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_auto_20170912_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='return_date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
