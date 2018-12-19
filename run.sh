#!/bin/bash

docker build -t asterisk . &&
  docker run -it --rm --net=host -v "$(pwd)"/asterisk:/etc/asterisk asterisk
