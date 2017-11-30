# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from managers.models import StatusDeletedModel, TimeHandlerModel
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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

    class Meta:
        db_table = "departements"

class Company(StatusDeletedModel, TimeHandlerModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    class Meta:
        db_table = "companies"

