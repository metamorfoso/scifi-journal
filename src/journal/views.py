from utilities.render import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Issue, Story, Cover
from num2words import num2words


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
        cover = Cover.objects.get(issue=current_issue)
        forthcoming_issue = num2words(current_issue.number + 1).title()
        stories = current_issue.story_set.all()
    else:
        current_issue = None
        forthcoming_issue = One
        stories = None
        cover = None

    return dict(
        current_issue=current_issue,
        forthcoming_issue=forthcoming_issue,
        stories=stories,
        landing_page=True,
        cover = cover
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
        
    cover = Cover.objects.get(issue=issue_number)    

    story_set = requested_issue.get_story_set().order_by('number')

    return dict(
        issue=requested_issue,
        stories=story_set,
        cover = cover
    )


def download_issue(request, issue_number, file_format):
    """
    View for downloading the Issue as a file in the specified format
    :param request:
    :param issue_number:
    :return file:
    """

    requested_issue = get_object_or_404(Issue, number=issue_number)
    file_contents = getattr(requested_issue, file_format)
    filename = "sponge-issue-%s.%s" % (str(requested_issue.number), file_format)

    response = HttpResponse(file_contents, content_type='application/%s' % file_format)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response


@render("journal/single_issue.html")
def current(request):
    """
    View for current issue

    :param request:
    :return:
    """

    current_issue = Issue.objects.filter(published=True).latest('pub_date')
    stories = current_issue.story_set.all().order_by('number')
    cover = Cover.objects.get(issue = current_issue)

    return dict(
        issue=current_issue,
        stories=stories,
        cover = cover
    )


@render("journal/story.html")
def view_story(request, slug):
    """
    View for displaying a PDF of a requested story

    :param request:
    :param slug:
    :return:
    """
    story = Story.objects.get(slug=slug)
    issue = story.issue    
    story_set = issue.story_set.all().order_by('number')

    return dict(
        story=story,
        issue=issue,        
        stories_in_issue=story_set
    )
