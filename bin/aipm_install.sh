#!/usr/bin/env bash

# get the root_dir for the tool, and save it in the config
now=$(cd `dirname $0`; pwd)
root_dir=$(cd $(dirname $now);  pwd)

ln -s $root_dir/bin/aipm.sh /usr/bin/aipm

docker pull aipm/base:cpu_0.0.1 &&
docker stop aipm_base &&
docker rm aipm_base &&
docker run -itd --name=aipm_base -v $root_dir:$root_dir --privileged=true aipm/base:cpu_0.0.1 /bin/bash


