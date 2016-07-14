from pages.models import Staff
from cms.models import Page


def common_context(request):
    context = dict()

    context['staff'] = Staff.objects.all()

    return context
