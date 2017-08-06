# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Item
# Create your views here.

def item(request):
    items = Item.status.all()

    context = {
        'items':items
    }

    return render(request, 'items.html', context)

def add_item(request):
    return render(request, 'items_form.html')
