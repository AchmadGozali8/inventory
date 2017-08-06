# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from companies.models import Departments, Company
from items.models import Item, ItemType

# Register your models here.

admin.site.register(Departments)
admin.site.register(Company)
admin.site.register(Item)
admin.site.register(ItemType)

