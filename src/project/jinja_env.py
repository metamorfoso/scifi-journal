from utilities import jinja_env
from django.core import urlresolvers


def environment(**options):
    env = jinja_env.environment(**options)
    env.globals.update({
        # project specific jinja env goes here
        'url_for': urlresolvers.reverse
    })
    return env
