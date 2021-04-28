#!/bin/bash

rm -rf ./uploads/
mkdir ./uploads
sudo gcsfuse --implicit-dirs --key-file /home/amokryshev/amokryshev-com-ed5e5b49836f.json -o allow_other amokryshev-com ./uploads
./shell_scripts/wait-for-it.sh ${DJ_DEFAULT_DB_HOST}:${DJ_DEFAULT_DB_PORT}
python manage.py create_or_use_db
python manage.py migrate
gunicorn --bind ${DJ_START_SERVER_AT_HOST} amokryshev.wsgi