# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_book_copy_no'),
    ]

    operations = [
        migrations.DeleteModel(
            name='book',
        ),
    ]
