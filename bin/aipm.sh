#!/usr/bin/env bash
option=$1
arg1=$2
arg2=$3

case $option in

    start)
        docker run -it aipm/dev:0.0.1 /bin/bash
        ;;
    listmodels)
        python /home/AIPM/src/listModels.py
        ;;
    install)
        if [ ! $arg1 ]; then
        echo 'Input the Model you are to install please. For example: aipm install fake_model1'
        elif [ ! $arg2 ]; then
        arg2='default'
        fi
        python /home/AIPM/src/InstallModel.py $arg1 $arg2
        ;;
    run)
        if [ ! $arg1 ]; then
        echo 'Input the model you are to run please.'
        fi
        if [ ! $arg2 ]; then
        echo 'Input the data you are to deal with please'
        fi
        docker start aipm_$arg1
        docker exec -t aipm_$arg1 python -W ignore /AIPM/src/getImageCategory.py $arg2
        ;;
    *)
        echo 'Illegal instruction, check your input please.'
        echo 'Maybe you need aipm -help'
    exit 
    ;;
    esac