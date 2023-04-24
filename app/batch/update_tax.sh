#!/usr/bin/env sh

PYTHONPATH=`pwd` python manage.py shell < products/tasks.py $@