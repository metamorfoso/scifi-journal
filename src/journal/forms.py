from django import forms
from .models import Submission, Submitter


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["title", "content"]


class SubmitterForm(forms.ModelForm):
    class Meta:
        model = Submitter
        fields = ["first_name", "last_name", "email_address"]
