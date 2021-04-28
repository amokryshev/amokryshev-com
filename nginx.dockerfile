##################### nginx ##########################
FROM nginx as nginx_img

RUN useradd -ms /bin/bash amokryshev

WORKDIR /home/amokryshev

COPY ./static ./static/
COPY ./nginx.conf ./
COPY ./shell_scripts/start_nginx_container.sh ./shell_scripts/
COPY ./shell_scripts/deploy_nginx_container.sh ./shell_scripts/
COPY ./amokryshev-com-ed5e5b49836f.json ./

ARG MV_RUN_SCRIPT_NGINX

ENV NG_LISTEN=${NG_LISTEN}
ENV NG_SERVER_NAME=${NG_SERVER_NAME}
ENV NG_PROXY_PASS=${NG_PROXY_PASS}
ENV NG_STATIC_EXPIRES=${NG_STATIC_EXPIRES}

RUN apt-get update
RUN apt-get install nano
RUN apt-get install sudo

# The way to install gcsfuse from repo, commented because of error: Malformed entry 1 in list file /etc/apt/sources.list.d/gcsfuse.list (Component)
# should be used in the future
#RUN export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
#RUN echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
#RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
#RUN apt-get update && sudo apt-get install gcsfuse

# Workaround to install gcsfuse
RUN sudo apt-get install fuse -y
RUN curl -L -O https://github.com/GoogleCloudPlatform/gcsfuse/releases/download/v0.34.1/gcsfuse_0.34.1_amd64.deb
RUN sudo dpkg --install gcsfuse_0.34.1_amd64.deb

RUN mkdir -p /var/nginx
RUN mkdir -p /var/cache/nginx/client_temp
RUN mkdir -p /var/cache/nginx/proxy_temp
RUN mkdir -p /var/cache/nginx/fastcgi_temp
RUN mkdir -p /var/cache/nginx/uwsgi_temp
RUN mkdir -p /var/cache/nginx/scgi_temp

RUN apt-get install acl
RUN setfacl -R -m u:amokryshev:rwx /etc/nginx
RUN setfacl -R -m u:amokryshev:rx /var
RUN setfacl -R -m u:amokryshev:rwx /var/log
RUN setfacl -R -m u:amokryshev:rwx /var/nginx
RUN setfacl -R -m u:amokryshev:rwx /var/run
RUN setfacl -R -m u:amokryshev:rx /var/cache
RUN setfacl -R -m u:amokryshev:rwx /var/run
RUN setfacl -R -m u:amokryshev:rwx /var/cache/nginx

RUN mv $MV_RUN_SCRIPT_NGINX run_nginx_container.sh
RUN chmod +x run_nginx_container.sh
RUN echo "amokryshev ALL=NOPASSWD: /usr/bin/gcsfuse, /usr/sbin/nginx, /usr/bin/tee" >> /etc/sudoers

USER amokryshev

CMD ./run_nginx_container.sh