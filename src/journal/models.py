from django.db import models
from num2words import num2words


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    bio = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Issue(models.Model):
    published = models.BooleanField(default=False)
    pub_date = models.DateField(verbose_name="issue publication date")
    number = models.IntegerField(verbose_name="issue number")
    introduction = models.TextField(max_length=500, blank=True)
    cover_image = models.ImageField(upload_to="cover_image_uploads/", blank=True)

    def __str__(self):
        return "issue %s" % str(self.number)

    @property
    def pretty_name(self):
        return "Issue %s" % num2words(self.number).title()

    @models.permalink
    def get_absolute_url(self):
        return "issue", (str(self.number),)

    def get_story_set(self):
        return self.story_set.all()


class Story(models.Model):
    issue = models.ForeignKey(Issue)
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to="story_uploads/")
    author_notes = models.TextField(blank=True, max_length=3000)

    class Meta:
        verbose_name_plural = "stories"

    def __str__(self):
        return self.title


# TODO: Review model
