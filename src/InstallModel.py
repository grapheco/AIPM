import requests
import sys
import os
import configparser
sys.path.append(os.path.abspath('.'))
from FetchModel import downloadModel
from FetchInfo import fetchInfo


# read the repo config
cp = configparser.ConfigParser()
cp.read(os.path.abspath('..')+'/setting.conf')
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
    version = cp_version.get(model_name, 'default')
else:
    version = sys.argv[2]

model_dir = repo_url + model_name +'/' + version # the model dir in the server system
model_url = model_dir + '/' + model_name + '.model'
dependency_url = model_dir + '/'+'dependency'
local_dependency_url = os.path.abspath('..')+"/model/"+model_name+'/'+version + '/dependency'

downloadModel(model_name,version, model_url);

# Download the dockerfile
r = requests.get(dependency_url)
if (r.status_code==404):
    exit("The resource doesn't exist, make sure your modelname and version are right.")
with open(local_dependency_url,"wb") as dependency:
    dependency.write(r.content)

#build the image and run the container
#stop the old container
os.system('docker stop aipm_'+model_name)
#remove the old image
os.system('docker rmi aipm:'+model_name)
os.system('docker build -t aipm:'+model_name+' -f '+local_dependency_url+' .')
#os.system('docker rm aipm_'+model_name)
os.system('docker run -itd --name=aipm_'+model_name+' -v /home/AIPM:/AIPM --privileged=true aipm:'+model_name+' /bin/bash')
