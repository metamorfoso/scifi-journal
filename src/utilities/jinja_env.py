from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.template import defaultfilters
from django.conf import settings

from jinja2 import Environment, Markup


def url(view, *args, **kwargs):
    """Match the less-verbose style of the django url templatetag."""
    return reverse(view, args=args, kwargs=kwargs)


def widget_type(bound_field):
    """Describe a form field's widget class, i.e. CheckboxInput.

       Used to render certain inputs differently in a generic form template."""
    return bound_field.field.widget.__class__.__name__


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': url,
    })
    for setting in ('STATIC_URL', 'DEBUG', 'TAKING_SUBMISSIONS'):
        env.globals.update({setting: getattr(settings, setting)})

    env.filters.update({
        'linebreaks': lambda val: Markup(defaultfilters.linebreaks(val)),
        'linebreaksbr': lambda val: Markup(defaultfilters.linebreaksbr(val)),
        'pluralize': defaultfilters.pluralize,
        'date': defaultfilters.date,
        'widget_type': widget_type,
    })

    return env
