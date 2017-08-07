# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Item
from django.http import HttpResponseRedirect
from form import ItemForm
# Create your views here.

def item(request):
    items = Item.status.all()
    context = {
        'items':items
    }
    return render(request, 'items.html', context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/inventory/')
    else:
        form = ItemForm()
        context = {
            'form': form
        }

    return render(request, 'items_form.html', context)

def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/')
    else:
        form = ItemForm()
        context = {
            "form": form,
            "pk": pk,
        }

    return render(request, 'item_update.html', context)

def delete_item(request, pk):
    deleted = 1
    not_deleted = 0

    item = get_object_or_404(Item, pk=pk)

    if item.deleted == not_deleted:
        post.deleted = deleted

    item.save()

    return HttpResponseRedirect('/inventory/')
