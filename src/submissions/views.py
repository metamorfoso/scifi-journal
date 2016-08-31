from utilities.render import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Submission, Submitter
from .forms import SubmissionForm, SubmitterForm


@render("django/submissions/submissions.html")
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
            # same Submitter instance; otherwise create new
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


@login_required()
@render("django/submissions/publish.html")
def publish(request):
    """
    View to confirm publication of a selection of submissions.
    :param request: with a querystring containing the ids of the submissions
    that are to be published.
    :return: queryset of submissions or HttpResponseRedirect to admin
    """

    ids = list(map(lambda item: int(item), request.GET["ids"].split(",")))
    submissions_to_publish = Submission.objects.filter(id__in=ids)

    # Handle confirmation
    if request.method == "POST":
        for submission in submissions_to_publish:
            submission.status = 3  # "Accepted" status
            submission.save()
        return HttpResponseRedirect("/admin/submissions/submission")

    return dict(
        submissions_to_publish=submissions_to_publish
    )
