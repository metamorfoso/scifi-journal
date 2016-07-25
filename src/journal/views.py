from utilities.render import render
from django.shortcuts import get_object_or_404
from .models import Issue, Submission, Submitter
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

    # Default context: empty forms for the Submission and Submitter
    context = dict(
        submitter_form=SubmitterForm(),
        submission_form=SubmissionForm()
    )

    # Handle form submission
    if request.method == "POST":
        submission_form = SubmissionForm(request.POST, request.FILES)
        submitter_form = SubmitterForm(request.POST)

        if submission_form.is_valid() and submitter_form.is_valid():
            submission_result = submission_form.cleaned_data
            submitter_result = submitter_form.cleaned_data

            # If this email address used to submit in the past, use
            # same Submitter instance
            new_submitter, created = Submitter.objects.get_or_create(
                email_address=submitter_result["email_address"]
            )

            # Save submission to db
            Submission.objects.create(
                title=submission_result["title"],
                content=submission_result["content"],
                author=new_submitter
            )

            # Update context dict and return it
            context["submission_successful"] = True
            return context

    else:
        return context
