# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-04 13:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20170804_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='deleted',
            field=models.IntegerField(choices=[(1, 'Not Deleted'), (0, 'Deleted')], default=1),
        ),
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 13, 58, 37, 744611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 13, 58, 37, 744611, tzinfo=utc)),
        ),
    ]
