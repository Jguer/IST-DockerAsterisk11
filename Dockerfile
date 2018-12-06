# Pull base image.
FROM ubuntu:14.04

ARG DEBIAN_FRONTEND=noninteractive
# Install.
RUN \
  apt-get update && \
  apt-get install -y asterisk asterisk-dahdi asterisk-mp3 asterisk-core-sounds-en asterisk-modules python-asterisk && \
  rm -rf /var/lib/apt/lists/*

# VOLUME ["/etc/asterisk", "/var/spool/asterisk", "/var/log/asterisk"]
VOLUME ["/etc/asterisk"]

COPY init.sh /tmp/
# Define default command.
CMD ["/bin/bash", "/tmp/init.sh"]

EXPOSE 5036
EXPOSE 5060
EXPOSE 10000-20000
