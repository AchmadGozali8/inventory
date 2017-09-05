# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

DELETED = 1
NOT_DELETED = 0

class StatusManager(models.Manager):
    def get_queryset(self):
        return super(StatusManager, self).get_queryset()\
                    .filter(deleted=NOT_DELETED)

class StatusDeletedModel(models.Model):
    status = StatusManager()
    objects = models.Manager()
    class Meta:
       abstract = True

class TimeHandlerModel(models.Model):
    created_at = models.DateTimeField(null=False, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
