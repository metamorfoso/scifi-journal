from django.db import models


class Submitter(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email_address = models.EmailField()

    def __str__(self):
        return self.email_address  # email is the only non-optional field


class Submission(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Submitter)
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to="submission_uploads/")
    author_notes = models.TextField(blank=True, max_length=3000)
    editor_notes = models.TextField(blank=True, max_length=3000)

    def __str__(self):
        return self.title