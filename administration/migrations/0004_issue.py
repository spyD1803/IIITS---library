# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20170911_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_rollno', models.CharField(max_length=80)),
                ('book_accn', models.IntegerField()),
                ('issue_date', models.DateTimeField(default=datetime.datetime(2017, 9, 11, 10, 22, 46, 756547), null=True)),
                ('return_date', models.DateTimeField(default=datetime.datetime(2017, 9, 11, 10, 22, 46, 756575), null=True)),
                ('fine', models.IntegerField(default=0)),
            ],
        ),
    ]