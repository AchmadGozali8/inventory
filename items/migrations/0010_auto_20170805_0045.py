# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-05 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20170805_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
