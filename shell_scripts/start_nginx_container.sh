#!/bin/bash

export DOLLAR="$"
envsubst < nginx.conf > /etc/nginx/nginx.conf
nginx -g 'daemon off;'