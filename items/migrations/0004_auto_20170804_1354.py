# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-04 13:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20170804_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemname',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 13, 54, 42, 245967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 13, 54, 42, 245083, tzinfo=utc)),
        ),
    ]
