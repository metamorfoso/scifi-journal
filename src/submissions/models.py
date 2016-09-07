from django.db import models
from django.core.urlresolvers import reverse
from journal.models import Story, Issue, Author


UNASSESSED = 0
SHORTLISTED = 1
REJECTED = 2
ACCEPTED = 3

SUBMISSION_STATES = (
    (UNASSESSED, "Unassessed"),
    (SHORTLISTED, "Shortlisted"),
    (REJECTED, "Rejected"),
    (ACCEPTED, "Accepted"),
)


class Submitter(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email_address = models.EmailField()

    def __str__(self):
        return self.email_address  # email is the only non-optional field

    @property
    def admin_url(self):
        return reverse("admin:submissions_submitter_change", args=(self.id,))

#     TODO: method to create Author instance based on Submitter


class Submission(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Submitter)
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to="submission_uploads/")
    author_notes = models.TextField(blank=True, max_length=3000)
    editor_notes = models.TextField(blank=True, max_length=3000)

    status = models.IntegerField(default=0, choices=SUBMISSION_STATES)

    archived = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def publish(self):
        # Update the appropriate fields on the Submission instance
        self.status = ACCEPTED
        self.published = True
        self.archived = True
        self.save()

        # Create a new Author instance based on the Submission's author (Submitter)
        author, created = Author.objects.get_or_create(
            first_name=self.author.first_name,
            last_name=self.author.last_name
        )

        # Create a new Story instance based on the Submission
        Story.objects.get_or_create(
            issue=Issue.objects.filter(published=False)[0],
            author=author,
            title=self.title,
            content=self.content,
            author_notes=self.author_notes
        )
        return
