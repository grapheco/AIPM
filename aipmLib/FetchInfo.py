import requests
import os
import configparser

dir = os.path.dirname(__file__)
root_dir = os.path.dirname(dir)

def fetchInfo(repo_url):
    local_info_url = root_dir+'/cache/version_info'
    if(os.path.exists(local_info_url)):
        os.remove(local_info_url)
    else:
        os.mknod(local_info_url)
        os.chmod(local_info_url, 0o755)
    r = requests.get(repo_url+'version_info')
    with open(local_info_url, "wb") as info:
        info.write(r.content)

    return local_info_url