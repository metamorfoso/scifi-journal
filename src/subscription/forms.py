from django import forms

class SubscriptionForm(forms.Form):
    email = forms.EmailField(max_length=254)