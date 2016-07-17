from utilities.render import render


@render("index.html")
def index(request):
    """
    Landing page for the issues app

    :param request:
    :return:
    """

    return dict(
        issues='issues'
    )