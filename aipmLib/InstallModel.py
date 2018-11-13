import requests
import sys
import os
import configparser

dir = os.path.dirname(__file__)
root_dir = os.path.dirname(dir)
sys.path.append(root_dir)
from aipmLib.FetchModel import downloadModel
from aipmLib.FetchInfo import fetchInfo


# read the config
cp = configparser.ConfigParser()
cp.read(os.path.dirname(dir)+'/config')
repo_url = cp.get('repo','url');


#fetch the version info
local_info_url = fetchInfo(repo_url)
# read the server version info
cp_version = configparser.ConfigParser()
cp_version.read(local_info_url)

# get the model name and version, default to be latest
model_name = sys.argv[1]
if(len(sys.argv) == 2 or sys.argv[2] == 'default'):
    print("No version input, default to be latest.");
    try:
        version = cp_version.get(model_name, 'default')
    except configparser.NoSectionError:
        exit("Can't find the version_info for your model, check your input please.")
else:
    version = sys.argv[2]

model_dir = repo_url + model_name +'/' + version # the model dir in the server system
model_url = model_dir + '/' + model_name + '.model'
dependency_url = repo_url + model_name + '/'+'dependency'
local_dependency_url = root_dir+'/model/'+model_name+ '/dependency'

downloadModel(model_name,version, model_url);
# Download the dockerfile

if(os.path.exists(root_dir+"/model/"+model_name+'/')==False):
        os.mkdir(root_dir+"/model/"+model_name+'/');
if(os.path.exists(local_dependency_url)==False):
        os.mknod(local_dependency_url)
r = requests.get(dependency_url)
if (r.status_code==404):
    exit("The resource doesn't exist, make sure your modelname and version are right.")
with open(local_dependency_url,"wb") as dependency:
    dependency.write(r.content)