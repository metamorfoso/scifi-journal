import os

PROJECT_ROOT = os.path.dirname(__file__)

bind = "127.0.0.1"
workers = 3
loglevel = "INFO"
proc_name = "django_sponge"
pidfile = os.path.join(PROJECT_ROOT, "gunicorn.pid")
errorlog = os.path.join(PROJECT_ROOT, "log", "gunicorn.log")
daemon = True  # fabfile.py provides methods for controlling the daemon
max_requests = 10000  # Prevent memory leaks from consuming all our resource
