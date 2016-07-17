from utilities.render import render
from .models import Issue, Story


@render("index.html")
def index(request):
    """
    Landing page for the issues app

    :param request:
    :return:
    """

    issues = Issue.objects.all()

    return dict(
        issues=issues
    )