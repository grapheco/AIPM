import requests
import sys
import os
import configparser
sys.path.append(os.path.abspath('.'))
from FetchModel import downloadModel
from FetchInfo import fetchInfo

# read the repo config
cp = configparser.ConfigParser()
cp.read('/AIPM/setting.conf')
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
local_dependency_url = "/AIPM/model/"+model_name+ '/dependency'

# Download the dockerfile
r = requests.get(dependency_url)
if (r.status_code==404):
    exit("The resource doesn't exist, make sure your modelname and version are right.")
with open(local_dependency_url,"wb") as dependency:
    dependency.write(r.content)

downloadModel(model_name,version, model_url);



