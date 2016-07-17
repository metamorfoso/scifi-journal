from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Issue(models.Model):
    pub_date = models.DateField(verbose_name='issue publication date')
    number = models.IntegerField(verbose_name='issue number')
    slug = AutoSlugField(populate_from=number, unique=True, always_update=True)

    def __str__(self):
        return "issue " + str(self.number)

    @models.permalink
    def get_absolute_url(self):
        return "issue", (self.slug,)

    def get_story_set(self):
        return self.story_set.all()


class Story(models.Model):
    issue = models.ForeignKey(Issue)
    submission_timestamp = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='submission_uploads/')

    def __str__(self):
        return self.title
