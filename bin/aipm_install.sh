#!/usr/bin/env bash

now=$(cd `dirname $0`; pwd -P) &&
root_dir=$(cd $(dirname $now);  pwd) &&

ln -fs $root_dir/bin/aipm.sh /usr/bin/aipm &&

docker pull aipm/base:cpu_0.0.1 &&
docker stop aipm_base &&
docker rm aipm_base &&
docker run -itd --name=aipm_base -v $root_dir:$root_dir --privileged=true aipm/base:cpu_0.0.1 /bin/bash


