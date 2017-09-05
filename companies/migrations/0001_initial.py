# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-22 16:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('deleted', models.IntegerField(choices=[(0, 'Not Deleted'), (1, 'Deleted')], default=0)),
            ],
            options={
                'db_table': 'comp',
            },
            managers=[
                ('status', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('deleted', models.IntegerField(choices=[(0, 'Not Deleted'), (1, 'Deleted')], default=0)),
            ],
            options={
                'db_table': 'departements',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='department',
            field=models.ForeignKey(db_column='department', on_delete=django.db.models.deletion.CASCADE, related_name='department_id', to='companies.Departments'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
