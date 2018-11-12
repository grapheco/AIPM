#!/usr/bin/env bash

model_name=$1
dependency_url=$2
docker stop aipm_$model_name | docker rmi aipm:$model_name |
docker build -t aipm:$model_name -f /home/AIPM/model/$model_name/dependency . &&
docker run -itd --name=aipm_$model_name -v /home/AIPM:/AIPM --privileged=true aipm:$model_name /bin/bash
echo run -itd --name=aipm_$model_name -v /home/AIPM:/AIPM --privileged=true aipm:$model_name /bin/bash