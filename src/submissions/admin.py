from django.contrib import admin
from django.core.urlresolvers import reverse
from .models import Submission, Submitter


class SubmissionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "author_link",
        "timestamp"
    ]
    list_select_related = True

    def author_link(self, submitter):
        url = reverse("admin:submissions_submitter_change", args=(submitter.id,))
        return '<a href="%s">%s</a>' % (url, "Go to author")
    author_link.allow_tags = True


admin.site.register(
    Submitter,
    list_display=["email_address", "first_name", "last_name"]
)

admin.site.register(
    Submission,
    SubmissionAdmin
)
