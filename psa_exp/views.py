#!/usr/bin/env python

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return HttpResponse("Hello World.")
