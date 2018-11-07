import requests
import sys
from contextlib import closing
import os
import configparser
sys.path.append(os.path.abspath('.'))

# read the config
cp = configparser.ConfigParser()
cp.read(os.path.abspath('..')+'/setting.conf')
repo_url = cp.get('repo', 'url');
info_url = repo_url+"/info"

with closing(requests.get(info_url)) as response:
    if(response.status_code==404):
        exit("The modelrepo you query doesn't exist. Check your input");

    info = response.content;
    # local cache the repo infomation
    local_tempInfo_url = os.path.abspath("..")+"/cache"+"tempInfo"
    if os.path.exists(local_tempInfo_url):
        os.remove(local_tempInfo_url);
    os.mknod(local_tempInfo_url)
    with(open(local_tempInfo_url,"wb")) as file:
        file.write(response.content)
    # TO DO: set the info in json format on server and parser the json locally
    for line in open(local_tempInfo_url):
        print(line)
    os.remove(local_tempInfo_url)
