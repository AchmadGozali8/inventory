# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from managers.models import StatusDeletedModel, TimeHandlerModel

import os

DELETED = 1
NOT_DELETED = 0

DELETED_STATUS = (
        (NOT_DELETED, "Not Deleted"),
        (DELETED, "Deleted"),
)

class ItemType(TimeHandlerModel):
    name = models.CharField(max_length=255)
    deleted = models.IntegerField(choices=DELETED_STATUS, default=NOT_DELETED)

    class Meta:
        db_table = "item_type"

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super(ItemType, self).save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return "{}".format(self.name)

class ItemCode(TimeHandlerModel):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ItemType, db_column="type")

    class Meta:
        db_table = "item_code"

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super(ItemCode, self).save(*args, **kwargs)

class Item(StatusDeletedModel, TimeHandlerModel):
    name = models.CharField(max_length=255)
    types = models.ForeignKey(ItemType, related_name="type_name", db_column='type')
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    deleted = models.IntegerField(choices=DELETED_STATUS, default=NOT_DELETED)

    class Meta:
        db_table = "items"
        ordering = ["-created_at", "-updated_at"]

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super(Item, self).save(*args, **kwargs)

