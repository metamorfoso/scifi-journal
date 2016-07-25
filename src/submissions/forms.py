from django import forms


class SubmissionForm(forms.Form):
    title = forms.CharField(max_length=100, label="Title")
    content = forms.FileField(label="File upload")


class SubmitterForm(forms.Form):
    email_address = forms.EmailField(label="Email address")
