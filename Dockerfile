# Pull base image.
FROM ubuntu:14.04

ARG DEBIAN_FRONTEND=noninteractive
# Install.
RUN \
  apt-get update && \
  apt-get install -y asterisk && \
  rm -rf /var/lib/apt/lists/*

COPY init.sh /tmp/

VOLUME ["/etc/asterisk", "/var/spool/asterisk", "/var/log/asterisk"]
# Define default command.
CMD ["/bin/bash", "/tmp/init.sh"]
