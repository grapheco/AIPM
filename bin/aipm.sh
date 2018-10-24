option=$1
arg=$2

case $option in
    -listModels)
        python /home/aipm_dev/src/listModels.py
        ;;
    -getModel)
        if [ ! $arg ]; then
        echo 'Input the Model you are to get please. For example: aipm getModel fake_model1'
        fi
        python /home/aipm_dev/src/getModel.py $arg
        ;;
    *)
        echo 'Illegal instruction, check your input please.'
        echo 'Maybe you need aipm help'
    exit 1
    ;;
    esac
