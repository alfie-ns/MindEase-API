#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
This script sets up the environment and executes administrative commands for a Django project.

- Sets the default Django settings module to 'main.settings'.
- Imports the Django execution function to start the server from `django.core.management`.
- if (Django NOT found; then raise ImportError.
- Execute command specified in the command-line arguments, such as 'runserver'.

"""
 
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it is installed and "
            "available on your PYTHONPATH environment variable. Have you "
            "activated the virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
