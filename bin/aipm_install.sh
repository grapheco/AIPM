#!/usr/bin/env bash

echo "alias aipm=/home/AIPM/bin/aipm.sh" >> /root/.bashrc
source ~/.bashrc
cd /home/AIPM
docker build -t aipm/base:cpu .