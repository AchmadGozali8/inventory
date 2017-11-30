# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login')
