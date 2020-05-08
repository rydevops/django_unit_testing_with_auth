FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.8

ARG UID="1000"
ARG GID="1000"
ARG USER="ryorke1"


# Setup container user with sudo access
RUN echo GID ${GID} UID ${UID} ${USER} && \
    groupadd --gid ${GID} ${USER} && \
    useradd --uid ${UID} --gid ${GID} -m ${USER} && \
    apt-get update && \
    apt-get install -y sudo && \
    echo ${USER} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER} && \
    echo export PATH=\$PATH:/home/ryorke1/.local/bin >> /home/ryorke1/.bashrc

USER $USER


