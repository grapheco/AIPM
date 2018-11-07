option=$1
arg1=$2
arg2=$3

case $option in
    # install)
    #     cd /home/aipm_dev
    #     docker build -t aipm/dev:0.0.1 .
    #     ;;
    start)
        docker run -it aipm/dev:0.0.1 /bin/bash
        ;;
    listmodels)
        python /home/aipm_dev/src/listModels.py
        ;;
    install)
        if [ ! $arg1 ]; then
        echo 'Input the Model you are to install please. For example: aipm install fake_model1'
        fi
        python /home/aipm_dev/src/getModel.py $arg1
        ;;
    run)
        if [ ! $arg1 ]; then
        echo 'Input the model you are to run please.'
        fi
        if [ ! $arg2 ]; then
        echo 'Input the data you are to deal with please'
        fi
        docker exec -t aipm_devtest01 python -W ignore /aipm_dev/src/getImageCategory.py $arg2 
        ;;
    *)
        echo 'Illegal instruction, check your input please.'
        echo 'Maybe you need aipm -help'
    exit 
    ;;
    esac
