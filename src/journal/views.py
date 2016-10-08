from utilities.render import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Issue, Story


@render("index.html")
def index(request):
    """
    Landing page for the site

    :param request:
    :return: dict of current issue and qs of its stories:
    """

    published_issues = Issue.objects.filter(published=True)
    if published_issues.exists():
        current_issue = published_issues.latest('pub_date')
        stories = current_issue.story_set.all()
    else:
        current_issue = None
        stories = None

    return dict(
        current_issue=current_issue,
        stories=stories,
        landing_page=True
    )


@render("journal/issue_archive.html")
def issue_archive(request):
    """
    View to display all issues available for viewing

    :param request:
    :return: dict of qs of all issues:
    """

    issues = Issue.objects.filter(published=True).order_by('-pub_date')

    return dict(
        issues=issues
    )


@render("journal/single_issue.html")
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


@render("journal/single_issue.html")
def current(request):
    """
    View for current issue

    :param request:
    :return:
    """

    current_issue = Issue.objects.filter(published=True).latest('pub_date')
    stories = current_issue.story_set.all()

    return dict(
        issue=current_issue,
        stories=stories
    )


@render("journal/story.hmtl")
def view_story(request, slug):
    """
    View for displaying a PDF of a requested story

    :param request:
    :param slug:
    :return:
    """
    story = Story.objects.get(slug=slug)
    issue = story.issue

    lines_to_exclude = ['\r', '\n', '\r\n']

    initial_lines = story.content.readlines()
    encoded_lines = list(map(lambda l: str(l, 'utf-8'), initial_lines))
    no_blanks = list(filter(lambda l: l not in lines_to_exclude, encoded_lines))

    return dict(
        story=story,
        issue=issue,
        paragraphs=no_blanks,
    )
