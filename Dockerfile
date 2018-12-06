# Pull base image.
FROM ubuntu:14.04

ARG DEBIAN_FRONTEND=noninteractive
# Install.
RUN \
  apt-get update && \
  apt-get install -y asterisk && \
  rm -rf /var/lib/apt/lists/*

COPY files/sip.conf files/extensions.conf files/init.sh /tmp/

# Add files.
ADD root/.bashrc /root/.bashrc
ADD root/.gitconfig /root/.gitconfig
ADD root/.scripts /root/.scripts

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

VOLUME ["/etc/asterisk", "/var/spool/asterisk", "/var/log/asterisk"]
# Define default command.
CMD ["/bin/bash", "/tmp/init.sh"]
