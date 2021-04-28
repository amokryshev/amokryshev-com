#!/bin/bash

mkdir ./uploads
sudo gcsfuse --implicit-dirs --key-file /home/amokryshev/amokryshev-com-ed5e5b49836f.json -o allow_other amokryshev-com ./uploads

export DOLLAR="$"
envsubst < nginx.conf | sudo tee /etc/nginx/nginx.conf
sudo nginx -g 'daemon off;'