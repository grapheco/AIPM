import requests
import os
def fetchInfo(repo_url):
    local_info_url = '/AIPM/cache/version_info'
    if(os.path.exists(local_info_url)):
        os.remove(local_info_url)
    else:
        os.mknod(local_info_url)

    r = requests.get(repo_url+'version_info')
    with open(local_info_url, "wb") as info:
        info.write(r.content)

    return local_info_url