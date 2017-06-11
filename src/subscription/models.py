from django.db import models
from verified_email_field.forms import VerifiedEmailField

class Subscriber(models.Model):
    email = VerifiedEmailField(label='email', required=True)
    def __str__(self):
        return self.email