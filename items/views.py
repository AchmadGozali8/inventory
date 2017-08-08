# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import Item
from django.http import HttpResponseRedirect
from form import ItemForm, ItemUpdateForm
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
        form = ItemUpdateForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/')
    else:
        form = ItemForm()
        form.fields['name'].widget.attrs['placeholder'] = item.name
        form.fields['types'].widget.attrs['placeholder'] = item.types
        form.fields['description'].widget.attrs['placeholder'] = item.description
        form.fields['location'].widget.attrs['placeholder'] = item.location 
        context = {
            "form": form,
            "pk": pk,
        }

    return render(request, 'items_update.html', context)

def delete_item(request, pk):
    deleted = 1
    not_deleted = 0

    item = get_object_or_404(Item, pk=pk)
    item.deleted = deleted
    item.save()

    return HttpResponseRedirect('/inventory/')
