{{ project_name|title }}
========================

You should write some docs, it's good for the soul.

Installation
------------

::

    $ django-admin.py startproject --template=<foo> -epy,rst

Usage
-----

To use ``django-admin.py`` to execute scripts you must explicitly include
the settings module to use with it, the default included settings are
``development`` and ``production`` so to start the development server you
would do::

    $ python django-admin.py --settings={{ project_name }}.settings.dev runserver
