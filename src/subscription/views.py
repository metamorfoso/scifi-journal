from django.shortcuts import render, render_to_response
from utilities.render import render
from .models import Subscriber

from subscription.forms import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm(request.POST)
    context = dict(
        type = 'subscribe',
        form = form
    )
    if form.is_valid():
        new_subscriber, created = Subscriber.objects.get_or_create(
                        email=form.cleaned_data['email']
                    )
        return render_to_response('subscribe/thanks.html', context)

@render("subscribe/thanks.html")        
def confirm(request):
    form = SubscriptionForm()
    return dict(
        form=form
    )

@render("subscribe/unsubscribe.html")
def unsubscribe(request):
    context = dict(
        type = subscribe,
        form = SubscriptionForm()
    )
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Subscriber.objects.filter(email=email):
                email_in_database = Subscriber.objects.filter(email=email)
                email_in_database.delete()
                context['type'] = 'unsubscribe'
            else:
                context['type'] = 'email_missing'
            return render_to_response('subscribe/thanks.html', context)

    else:
        return context
