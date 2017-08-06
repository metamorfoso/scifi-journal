from django.db import models
from num2words import num2words
from autoslug import AutoSlugField
import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    bio = models.TextField(max_length=250, blank=True)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Issue(models.Model):
    published = models.BooleanField(default=False)
    pub_date = models.DateField(verbose_name="issue publication date", blank=True, null=True)
    number = models.IntegerField(verbose_name="issue number")
    introduction = models.TextField(max_length=500, blank=True)
    bandcamp_album_id = models.IntegerField(blank=True, null=True)
    bandcamp_album_url = models.CharField(max_length=100,blank=True)

    pdf = models.FileField(verbose_name="issue as PDF document", blank=True, null=True)
    mobi = models.FileField(verbose_name="issue as Mobi document", blank=True, null=True)
    epub = models.FileField(verbose_name="issue as an epub document", blank=True, null=True)

    def __str__(self):
        return "issue %s" % str(self.number)

    @property
    def pretty_name(self):
        return "Issue %s" % num2words(self.number).title()

    @property
    def pretty_pub_date(self):
        return "%s, %s" % (self.pub_date.strftime("%B"), self.pub_date.year)

    @models.permalink
    def get_absolute_url(self):
        return "issue", (str(self.number),)

    def get_story_set(self):
        return self.story_set.all()

    def has_pdf(self):
        return self.pdf == True


def autoslug_populate_from(instance):
    return instance.title


class Story(models.Model):
    issue = models.ForeignKey(Issue)
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=30000, blank=True)
    author_notes = models.TextField(blank=True, max_length=3000)
    number = models.IntegerField()
    bandcamp_track_id = models.CharField(max_length=11,blank=True,null=True)

    slug = AutoSlugField(
        populate_from=autoslug_populate_from,
        unique_with=['author__first_name', 'author__last_name'],
        always_update=True
    )

    class Meta:
        verbose_name_plural = "stories"

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return "view_story", (self.slug,)


class Cover(models.Model):
    cover_image = models.ImageField(upload_to="cover_image_uploads/", blank=True)
    issue = models.ForeignKey(Issue)
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    artist_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
