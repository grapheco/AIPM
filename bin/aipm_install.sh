#!/usr/bin/env bash

now=$(cd `dirname $0`; pwd -P) &&
root_dir=$(cd $(dirname $now);  pwd) &&

ln -fs $root_dir/bin/aipm.sh /usr/local/bin/aipm &&

docker pull aipm/base:cpu_0.0.1 &&
docker kill aipm_base ;
docker rm aipm_base ;
docker run -itd --name=aipm_base -v $root_dir:$root_dir --privileged=true aipm/base:cpu_0.0.1 /bin/bash


