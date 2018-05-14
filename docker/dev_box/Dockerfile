FROM ubuntu:16.04
RUN rm -rf /var/lib/apt/lists/* &&\
    apt-get update --fix-missing

# Install apt packages and configure them
RUN apt-get install -y git sudo vim curl tree less python-pip python3-pip python-dev python3-dev

# Install docker
RUN cd /tmp && curl -fsSL get.docker.com -o get-docker.sh &&\
    sudo sh get-docker.sh

# Create user and set it as default
ARG DEVBOX_USER_NAME
ARG DEVBOX_USER_UID
ARG DEVBOX_USER_GUID
ARG DEVBOX_PWD
RUN useradd -d /home/$DEVBOX_USER_NAME -m $DEVBOX_USER_NAME &&\
    usermod -u $DEVBOX_USER_UID -U $DEVBOX_USER_NAME &&\
    usermod -aG sudo $DEVBOX_USER_NAME &&\
    groupmod -g $DEVBOX_USER_GUID $DEVBOX_USER_NAME &&\
    echo $DEVBOX_USER_NAME:$DEVBOX_USER_NAME | chpasswd &&\
    usermod -aG docker $DEVBOX_USER_NAME &&\
    echo "$DEVBOX_USER_NAME ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers

RUN mkdir /venv &&\
    chown $DEVBOX_USER_NAME:$DEVBOX_USER_NAME /venv &&\
    pip install pipenv

USER $DEVBOX_USER_NAME
ENV WORKON_HOME /venv
RUN mkdir -p $DEVBOX_PWD && cd $DEVBOX_PWD && pwd && pipenv --three
WORKDIR $DEVBOX_PWD
ADD Pipfile .
ADD Pipfile.lock .
RUN pipenv install && pipenv install -d

# Create entrypoint
USER root
COPY docker/dev_box/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# CleanUP
RUN sudo rm -rf /tmp/* &&\
    sudo rm -rf /root/.cache/* &&\
    sudo rm -rf /var/lib/apt/lists/*

# set user
USER $DEVBOX_USER_NAME
WORKDIR /home/$DEVBOX_USER_NAME