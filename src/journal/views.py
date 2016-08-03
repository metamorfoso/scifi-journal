from utilities.render import render
from django.shortcuts import get_object_or_404
from .models import Issue


@render("django/index.html")
def index(request):
    """
    Landing page for the site

    :param request:
    :return: dict of current issue and qs of its stories:
    """

    current_issue = Issue.objects.filter(published=True).latest('pub_date')
    stories = current_issue.story_set.all()

    return dict(
        current_issue=current_issue,
        stories=stories
    )


@render("django/issue/issue_archive.html")
def issue_archive(request):
    """
    View to display all issues available for viewing

    :param request:
    :return: dict of qs of all issues:
    """

    issues = Issue.objects.filter(published=True)

    return dict(
        issues=issues
    )


@render("django/issue/single_issue.html")
def single_issue(request, issue_number):
    """
    View to display individual issues

    :param request:
    :param issue_number:
    :return: requested issue instance and a qs of its stories:
    """

    requested_issue = get_object_or_404(Issue, number=issue_number)

    story_set = requested_issue.get_story_set()

    return dict(
        issue=requested_issue,
        stories=story_set
    )


@render("django/about.html")
def about(request):
    """
    An about page for the journal

    :param request:
    :return:
    """

    return dict()

