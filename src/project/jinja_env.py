from utilities import jinja_env


def environment(**options):
    env = jinja_env.environment(**options)
    env.globals.update({
        # project specific jinja env goes here
    })
    return env
