from utilities.render import render
from django.shortcuts import get_object_or_404
from .models import Issue


@render("django/index.html")
def index(request):
    """
    Landing page for the site

    :param request:
    :return:
    """

    current_issue = Issue.objects.latest('pub_date')

    return dict(
        current_issue=current_issue
    )


@render("django/issue/all_issues.html")
def all_issues(request):
    """
    View to display all issues available for viewing

    :param request:
    :return: qs of all issues
    """

    issues = Issue.objects.all()

    return dict(
        issues=issues
    )


@render("django/issue/single_issue.html")
def single_issue(request, issue_number):
    """
    View to display individual issues

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
