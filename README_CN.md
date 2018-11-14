# AIPM

**AIPM**(Artificial Intelligence Package Management)是一个可以帮助您从远端仓库安装人工智能相关模型，并在本地运行的工具。
在AIPM的帮助下，您将不用关心复杂的环境问题以及模型管理问题，从而把更多精力投入到数据处理中去。


### 要求

#### 硬件:
- 20G 或更多的磁盘空间
- 8G 或更大的运行内存

#### 软件:
- Docker 18.06.1-ce 或更新的ce版
- CentOS 7 或更新的稳定版
- Git
- python 

### 构建说明：
``` 
git clone https://github.com/Airzihao/AIPM.git
bash ../AIPM/bin/aipm_install.sh 
```

根据您的网络环境，构建过程可能花费大约15分钟，请耐心等待，不要终止安装进程。


### 运行命令

```angular2html
aipm install DogOrCat 0.0.1 #t版本号可以省略，当未指明版本号时，默认安装最新版本。
aipm run DogOrCat ../AIPM/data/images #输入数据支持文件或路径，但请使用绝对路径。
```

