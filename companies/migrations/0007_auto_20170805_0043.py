# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-05 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20170804_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='deleted',
            field=models.IntegerField(choices=[(0, 'Not Deleted'), (1, 'Deleted')], default=0),
        ),
        migrations.AlterField(
            model_name='departments',
            name='deleted',
            field=models.IntegerField(choices=[(0, 'Not Deleted'), (1, 'Deleted')], default=0),
        ),
    ]
