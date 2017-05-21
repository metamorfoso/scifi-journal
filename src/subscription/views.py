from django.shortcuts import render, HttpResponseRedirect
from utilities.render import render
from .models import Subscriber

from subscription.forms import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect('/thanks')

@render("subscribe/thanks.html")        
def confirm(request):
    form = SubscriptionForm()
    return dict(
        form=form
    )
        

        
