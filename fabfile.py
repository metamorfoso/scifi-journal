from fabric.api import run, local, env, task
from fabric.context_managers import cd, prefix, settings
from fabric.contrib.files import exists
import logging
from functools import partial


@task
def prod():
    env.shell = "/bin/bash -l -i -c"
    env.hosts = ['ubuntu@52.62.2.21']
    env.project = "/home/ubuntu/sponge/scifi-journal"
    env.virtualenv = "sponge"
    env.workon = "workon %s" % env.virtualenv

@task
def update():
    """
    Sync the git repos
    """
    if env.get('project', False):
        with cd(env.project):
            run('git pull')

@task
def deploy(no_migrate=False):

    update()

    with cd(env.project), prefix(env.workon):
        run('pip install -r requirements.txt --upgrade')
        if not no_migrate:
            run('./manage.py migrate')
        run('npm install')
        run('npm run clean')
        run('npm run dist')
        run('./manage.py collectstatic --noinput')

    clear_cache()
    restart()


@task
def clear_cache():
    with cd(env.project), prefix(env.workon):
        run('DJANGO_SETTINGS_MODULE=project.settings '
            'python -c "from django.core.cache import cache; '
            'cache.clear()"')


def send_signal(signal):
    pid_path = "%s/gunicorn.pid" % env.project
    if exists(pid_path):
        run("kill -%s `cat %s`" % (signal, pid_path))
    else:
        logging.warning("The process id is missing!")


restart = partial(send_signal, "HUP")
restart.__doc__ = "Reload graciously"
restart = task(restart)

gunicorn_stop = partial(send_signal, "TERM")
gunicorn_stop.__doc__ = "Shutdown graciously"
gunicorn_stop = task(gunicorn_stop)

gunicorn_kill = partial(send_signal, "KILL")
gunicorn_kill.__doc__ = "Terminate and kill the server process"
gunicorn_kill = task(gunicorn_kill)


@task
def gunicorn_start():
    with cd(env.project), prefix(env.workon):
        run("gunicorn project.wsgi -c gunicorn.conf.py")
