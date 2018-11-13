#!/usr/bin/env bash

model_name=$1
dependency_url=$2

now=$(cd `dirname $0`; pwd -P) &&
root_dir=$(cd $(dirname $now);  pwd)

docker stop aipm_$model_name ; docker rmi aipm:$model_name ;
docker rm aipm_$model_name ;
docker build -t aipm:$model_name -f $root_dir/model/$model_name/dependency . &&
docker run -itd --name=aipm_$model_name -v $root_dir:$root_dir --privileged=true aipm:$model_name /bin/bash