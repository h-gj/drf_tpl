#!/bin/bash

python /drf_tpl/manage.py makemigrations&&
python /drf_tpl/manage.py migrate&&
uwsgi --ini /drf_tpl/deploy/uwsgi.ini&&
tail -f /dev/null

exec "$@"

