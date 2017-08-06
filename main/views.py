# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from items.models import Item
# Create your views here.

def item(request):
    items = Item.status.all()

    context = {
        'items': items
    }

    return render(request, 'items.html', context)
