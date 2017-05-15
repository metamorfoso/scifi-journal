from django.shortcuts import render, HttpResponseRedirect
from .models import Subscriber

from .forms import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect('/thanks/')
    else:
        return HttpResponseRedirect('/thanks/')
        
