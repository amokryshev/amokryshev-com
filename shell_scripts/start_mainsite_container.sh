#!/bin/bash

./shell_scripts/wait-for-it.sh ${DJ_DEFAULT_DB_HOST}:${DJ_DEFAULT_DB_PORT}
python manage.py create_or_use_db
python manage.py migrate
gunicorn --bind ${DJ_START_SERVER_AT_HOST} amokryshev.wsgi