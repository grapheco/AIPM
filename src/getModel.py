import requests
import sys
from contextlib import closing
import os
import configparser
sys.path.append(os.path.abspath('.'))
import ProgressBar

# read the config
cp = configparser.ConfigParser()
cp.read(os.path.abspath('..')+'/setting.conf')
repo_url = cp.get('repo','url');

# get the model name, for example: my_model_alex.h5
model_name = sys.argv[1]

#get the model url and local_model_url
model_url = repo_url + model_name # the model url in the server system
local_model_url=os.path.abspath('..')+"/model/"+model_name  #the model url in the client system

# never download for twice
if( os.path.exists(local_model_url)):
    exit("The "+model_name+" is already in your system. No need to download once more");

# get the response head and get the content_size
with closing(requests.get(model_url, stream=True)) as response:
    chunk_size = 1024*1024  #unit:kB
    content_size = int(response.headers['content-length']) # unit: B

    if(response.status_code==404):
        exit("The model you required doesn't exist. Check your input");

    os.mknod(local_model_url)
    sum = 0
    with open(local_model_url, "wb") as file:
       for data in response.iter_content(chunk_size=chunk_size):
           file.write(data)
           sum += len(data)
           ProgressBar.view_bar(sum,content_size);
    print('\n')
    print("Module "+model_name+" installed.");
