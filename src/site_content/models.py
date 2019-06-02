from django.db import models

from froala_editor.fields import FroalaField

class About(models.Model):
    contents = models.TextField(max_length=30000, blank=True)

    class Meta:
        verbose_name_plural = "About"

class Submission_Guidelines(models.Model):
    general = models.TextField(max_length=30000, blank=True)
    submissions = models.TextField(max_length=30000, blank=True)
    formatting = models.TextField(max_length=30000, blank=True)
    content = models.TextField(max_length=30000, blank=True)
    contact = models.TextField(max_length=30000, blank=True)

    class Meta:
        verbose_name_plural = "Submission Guidelines"
