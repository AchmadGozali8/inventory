# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-06 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_auto_20170806_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='types',
            field=models.ForeignKey(db_column='type', on_delete=django.db.models.deletion.CASCADE, related_name='types_name', to='items.ItemType'),
        ),
    ]
