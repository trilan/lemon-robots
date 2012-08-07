#!/bin/bash

set -e

export PYTHONPATH=$PWD/..:$PYTHONPATH

django-admin.py test --settings=tests.settings robots
django-admin.py test --settings=tests.settings_views test_views
