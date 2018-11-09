import requests
import sys
from contextlib import closing
import os
sys.path.append(os.path.abspath('.'))
import ProgressBar

def downloadModel(model_name, version, model_url):

    # the model url in the client system
    local_model_dir=os.path.abspath('..')+"/model/"+model_name+'/'+ version + '/'
    local_model_url= local_model_dir + model_name+'.model'

    # never download for twice
    if( os.path.exists(local_model_url)):
        exit("The "+model_name+" is already in your system. No need to download once more");

    # get the response head and get the content_size
    with closing(requests.get(model_url, stream=True)) as response:
        chunk_size = 1024*1024  #unit:kB
        content_size = int(response.headers['content-length']) # unit: B

        if(response.status_code==404):
            print(model_url)
            exit("The model you required doesn't exist. Check your input");

        if(os.path.exists(os.path.abspath('..')+"/model/"+model_name+'/')==False):
            os.mkdir(os.path.abspath('..')+"/model/"+model_name+'/');
        if(os.path.exists(local_model_dir)==False):
            os.mkdir(local_model_dir)
        os.mknod(local_model_url)
        sum = 0
        with open(local_model_url, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                sum += len(data)
                ProgressBar.view_bar(sum,content_size);
        print('\n')
        print("Module "+model_name+" installed.");
