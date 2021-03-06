from utilities.render import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from .models import Issue, Story, Cover
from site_content.models import About
from num2words import num2words
from subscription.forms import SubscriptionForm
import requests
from datetime import datetime

def get_recent_instagram_post():
    url = 'https://api.instagram.com/v1/users/13938718211/media/recent'
    params = {
        "access_token": '13938718211.473bf93.990be13111e047f89dc528820097681d',
        "count": 1
    }
    response = requests.get(url, params=params)
    json = response.json()
    data = json['data'][0]
    caption = data['caption']['text']
    created_at = data['caption']['created_time']
    link = data['link']
    image = data['images']['standard_resolution']['url']
    formatted_created_at = datetime.utcfromtimestamp(int(created_at)).strftime('%Y-%m-%dT%H:%M:%SZ')
    return dict(
            caption = caption,
            created_at = created_at,
            link = link,
            image = image
            )

@render("index.html")
def index(request):
    """
    Landing page for the site

    :param request:
    :return: dict of current issue and qs of its stories:
    """

    about = About.objects.first()

    published_issues = Issue.objects.filter(published=True)
    if published_issues.exists():
        current_issue = published_issues.latest('pub_date')
        cover = Cover.objects.filter(issue=current_issue).first()
        forthcoming_issue = num2words(current_issue.number + 1).title()
        stories = current_issue.story_set.all()
    else:
        current_issue = None
        forthcoming_issue = 'One'
        stories = None
        cover = None

    form = SubscriptionForm()

    return dict(
        about=about,
        current_issue=current_issue,
        forthcoming_issue=forthcoming_issue,
        stories=stories,
        landing_page=True,
        cover=cover,
        form=form,
        recent_instagram_post = get_recent_instagram_post()
        )


@render("journal/issue_archive.html")
def issue_archive(request):
    """
    View to display all issues available for viewing

    :param request:
    :return: dict of qs of all issues:
    """

    issues = Issue.objects.filter(published=True).order_by('-pub_date')
    form = SubscriptionForm()

    return dict(
        issues=issues,
        form=form
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
    cover = Cover.objects.filter(issue=requested_issue).first()
    story_set = requested_issue.get_story_set().order_by('number')

    form = SubscriptionForm()
    if not requested_issue.published:
      raise Http404()

    return dict(
        issue=requested_issue,
        stories=story_set,
        cover=cover,
        form=form
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
    cover = Cover.objects.filter(issue=current_issue).first()
    form = SubscriptionForm()

    height_of_bandcamp_plugin = 120
    for story in stories:
        if story.bandcamp_track_id:
            height_of_bandcamp_plugin += 40


    return dict(
        issue=current_issue,
        stories=stories,
        cover=cover,
        form=form,
        height_of_bandcamp_plugin=str(height_of_bandcamp_plugin) + "px"
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
    if not issue.published:
        raise Http404
    story_set = issue.story_set.all().order_by('number')
    form = SubscriptionForm()

    return dict(
        story=story,
        issue=issue,
        stories_in_issue=story_set,
        form=form
    )
