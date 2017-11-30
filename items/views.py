# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from models import Item
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms.item_form import ItemForm, ItemUpdateForm

@login_required
def item(request):
    items = Item.status.all()
    context = {
        'items':items
    }
    request.session['item_count'] = items.count()
    return render(request, 'items.html', context)

def code_item(item_type):
    count = Item.objects.filter(types__exact=item_type).count()
    count = count + 1
    item_type = str(item_type)
    string_slice = item_type[0:3]
    concatenate = "{}{}".format(string_slice,count)
    return concatenate

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.code = code_item(instance.types)
            instance.save()
            return HttpResponseRedirect('/inventory/')
    else:
        form = ItemForm()
        context = {
            'form': form
        }

    return render(request, 'items_form.html', context)

@login_required
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

@login_required
def delete_item(request, pk):
    deleted = 1
    not_deleted = 0

    item = get_object_or_404(Item, pk=pk)
    item.deleted = deleted
    item.save()

    return HttpResponseRedirect('/inventory/')
