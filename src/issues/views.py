from utilities.render import render
from django.shortcuts import get_object_or_404
from .models import Issue, Story


@render("django/index.html")
def index(request):
    """
    Landing page for the issues app

    :param request:
    :return: qs of all issues
    """

    issues = Issue.objects.all()

    return dict(
        issues=issues
    )


@render("django/issue/issue.html")
def issue(request, issue_number):
    """
    Page for viewing individual issues of the journal

    :param request:
    :param issue_number:
    :return: requested issue instance
    """

    requested_issue = get_object_or_404(Issue, number=issue_number)

    story_set = requested_issue.get_story_set()

    return dict(
        issue=requested_issue,
        stories=story_set
    )
