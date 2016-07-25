from utilities.render import render
from .models import Submission, Submitter
from .forms import SubmissionForm, SubmitterForm


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
