#!/bin/bash

set -e

export PYTHONPATH=$PWD/..:$PYTHONPATH

django-admin.py test --settings=tests.settings robots
django-admin.py test --settings=tests.settings_views test_views
django-admin.py test --settings=tests.settings_django_admin test_django_admin
django-admin.py test --settings=tests.settings_lemon_admin test_lemon_admin
