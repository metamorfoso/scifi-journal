from django.db import models

from froala_editor.fields import FroalaField

class About(models.Model):
    contents = FroalaField(blank=True)

    class Meta:
        verbose_name_plural = "About"

class Submission_Guidelines(models.Model):
    general = FroalaField(blank=True)
    submissions = FroalaField(blank=True)
    formatting = FroalaField(blank=True)
    content = FroalaField(blank=True)
    contact = FroalaField(blank=True)

    class Meta:
        verbose_name_plural = "Submission Guidelines"