##################### mainsite ##########################
FROM python:latest as mainsite_img

RUN useradd -ms /bin/bash amokryshev

WORKDIR /home/amokryshev

COPY . ./

ARG MV_RUN_SCRIPT_MAINSITE
ARG DEBIAN_FRONTEND=noninteractive

ENV DJ_DEBUG="${DJ_DEBUG_PROD}"
ENV DJ_SECRET_KEY="${DJ_SECRET_KEY}"
ENV DJ_START_SERVER_AT_HOST="${DJ_START_SERVER_AT_HOST}"
ENV DJ_ALLOWED_HOSTS="${DJ_ALLOWED_HOSTS_PROD}"
ENV DJ_DEFAULT_DB_NAME="${DJ_DEFAULT_DB_NAME}"
ENV DJ_DEFAULT_DB_USER="${DJ_DEFAULT_DB_USER}"
ENV DJ_DEFAULT_DB_PASS="${DJ_DEFAULT_DB_PASS_PROD}"
ENV DJ_DEFAULT_DB_HOST="${DJ_DEFAULT_DB_HOST_PROD}"
ENV DJ_DEFAULT_DB_PORT=${DJ_DEFAULT_DB_PORT}
ENV DJ_ADM_DB_NAME="${DJ_ADM_DB_NAME}"
ENV DJ_ADM_DB_USER="${DJ_ADM_DB_USER}"
ENV DJ_ADM_DB_PASS="${DJ_ADM_DB_PASS_PROD}"
ENV DJ_ADM_DB_HOST="${DJ_ADM_DB_HOST_PROD}"
ENV DJ_ADM_DB_PORT=${DJ_ADM_DB_PORT}
ENV DJ_CACHE_URL="${DJ_CACHE_URL_PROD}"
ENV DJ_CACHE_PREFIX="${DJ_CACHE_PREFIX}"
ENV DJ_CACHE_TIMEOUT=${DJ_CACHE_TIMEOUT}
ENV DJ_AN="${DJ_AN}"
ENV DJ_AE="${DJ_AE}"
ENV DJ_AP="${DJ_AP}"

RUN apt-get update
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
RUN mv $MV_RUN_SCRIPT_MAINSITE run_mainsite_container.sh
RUN apt-get install acl
RUN setfacl -R -m u:amokryshev:rx /home
RUN setfacl -R -m u:amokryshev:rwx /home/amokryshev/
#RUN setfacl -R -m u:amokryshev:rwx /home/amokryshev/uploads/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x run_mainsite_container.sh
RUN echo "amokryshev ALL=NOPASSWD: /usr/bin/gcsfuse" >> /etc/sudoers

USER amokryshev

CMD ./run_mainsite_container.sh