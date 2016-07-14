#!/usr/bin/env python
import os
import sys

# uncomment this to raise an exception for all warnings
# import warnings
# warnings.filterwarnings("error")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
