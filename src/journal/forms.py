from django import forms
from .models import Submission, Submitter


# class SubmissionForm(forms.ModelForm):
#     class Meta:
#         model = Submission
#         fields = ["title", "content"]
#
#
# class SubmitterForm(forms.ModelForm):
#     class Meta:
#         model = Submitter
#         fields = ["first_name", "last_name", "email_address"]


class SubmissionForm(forms.Form):
    title = forms.CharField(max_length=100, label="Title")
    content = forms.FileField(label="File upload")


class SubmitterForm(forms.Form):
    email_address = forms.EmailField(label="Email address")
