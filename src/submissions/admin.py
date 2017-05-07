from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from .models import Submission, Submitter


# Actions for mass-setting status
def mass_set_unassessed(modeladmin, request, qs):
    qs.update(status=0)
mass_set_unassessed.short_description = "Revert to 'unassessed'"


def mass_set_shortlisted(modeladmin, request, qs):
    qs.update(status=1)
mass_set_shortlisted.short_description = "Shortlist"


def mass_set_rejected(modeladmin, request, qs):
    qs.update(status=2)
mass_set_rejected.short_description = "Reject"


def mass_set_accepted(modeladmin, request, qs):
    qs.update(status=3)
mass_set_accepted.short_description = "Accept"


def publish_selected(modeladmin, request, qs):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    return HttpResponseRedirect("/confirm_publication/?ids=%s" % (",".join(selected)))
publish_selected.short_description = "Publish"


class SubmissionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "author_link",
        "timestamp",
        "status",
        "archived",
        "published"
    ]
    list_select_related = True

    list_editable = [
        "status",
        "archived"
    ]
    actions = [
        mass_set_unassessed,
        mass_set_shortlisted,
        mass_set_rejected,
        mass_set_accepted,
        publish_selected
    ]
    list_filter = [
        "archived",
        "status"
    ]

    def author_link(self, submission):
        url = reverse("admin:submissions_submitter_change", args=(submission.author.id,))
        return '<a href="%s">%s</a>' % (url, "Go to submitter")
    author_link.allow_tags = True


admin.site.register(
    Submitter,
    list_display=["email_address", "first_name", "last_name"]
)

admin.site.register(
    Submission,
    SubmissionAdmin
)
