# AIPM

如果您习惯于阅读中文版自述文件，请移步[README_CN.md](https://github.com/Airzihao/AIPM/blob/master/README_CN.md)。

Artificial Intelligence Package Management is a 
powerful tool, which can help you to install models from
repo server, and run it locally.

With the help of AIPM, you don't need to care about the 
complex environment problem.


### Requirement



#### Hardware:
- 20G or more space on disk
- 8G or more RAM


#### Software:
- Docker 18.06.1-ce or later ce version
- CentOS 7 or later stable version
- Git
- python 



### Build instruction：
``` 
git clone https://github.com/Airzihao/AIPM.git
sudo bash ../AIPM/bin/aipm_install.sh 
```
Depending on your network, the install progress may take about 15mins, be patient and don't kill the install process.


### Commands

```angular2html
aipm install DogOrCat 0.0.1 #If the version number is unsigned, the latest version will be installed.
aipm run DogOrCat ../AIPM/data/images #You can input filename or a dir including the data, but use absolute dir please.
```
Make sure the login user is added into the docker user group, or it requires sudo permission to run the aipm command.

You can use the following commands to add the login user into the docker user group.
```
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
```


