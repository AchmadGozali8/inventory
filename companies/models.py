# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from managers.models import StatusDeletedModel, TimeHandlerModel

DELETED = 1
NOT_DELETED = 0

DELETED_STATUS = (
        (NOT_DELETED, "Not Deleted"),
        (DELETED, "Deleted"),
)

class Departments(TimeHandlerModel):
    name = models.CharField(max_length=255)
    deleted = models.IntegerField(choices=DELETED_STATUS, default=NOT_DELETED)

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super(Departments, self).save(*args, **kwargs)

class Company(StatusDeletedModel, TimeHandlerModel):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Departments, related_name="department_id",
                                   db_column="department")
    deleted = models.IntegerField(choices=DELETED_STATUS, default=NOT_DELETED)

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super(Company, self).save(*args, **kwargs)


