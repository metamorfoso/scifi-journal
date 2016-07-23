from utilities.render import render
from django.shortcuts import get_object_or_404, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Issue
from .forms import SubmissionForm, SubmitterForm


@render("django/index.html")
def index(request):
    """
    Landing page for the site

    :param request:
    :return:
    """

    current_issue = Issue.objects.latest('pub_date')
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


@render("django/about.html")
def about(request):
    """
    An about page for the journal

    :param request:
    :return:
    """

    return dict()


@render("django/submissions.html")
def submissions(request):
    """
    Submissions portal

    :param request:
    :return:
    """

    response = dict(
        submission_successful=False,
        submitter_form=SubmitterForm().as_ul(),
        submission_form=SubmissionForm().as_ul()
    )

    if request.method == "POST":
        submission_form = SubmissionForm(request.POST, request.FILES)
        submitter_form = SubmitterForm(request.POST)

        # Check that forms are valid
        if submitter_form.is_valid() and submission_form.is_valid():
            new_submission = submission_form.save(commit=False)
            new_submitter = submitter_form.save(commit=False)

            print(new_submission, new_submitter)

            # On success, return submission_successful=True (so template can display the
            # thank-you message), and fresh empty forms.
            response["submission_successful"] = True

            return response

    return response
