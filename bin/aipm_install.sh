#!/usr/bin/env bash

echo "alias aipm=/home/AIPM/bin/aipm.sh" >> /root/.bashrc

service docker start

cd /home/AIPM

docker pull aipm/base:cpu_0.0.1 &&
docker run -itd --name=aipm_base -v /home/AIPM:/AIPM --privileged=true aipm/base:cpu_0.0.1 /bin/bash

source ~/.bashrc