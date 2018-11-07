# version: 0.0.1
From ubuntu:18.04

MAINTAINER airzihao

RUN apt update
RUN apt-get install -y wget
RUN apt-get install -y vim
# RUN cd /home \
#     && wget --quiet https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh
# RUN bash /home/Anaconda3-5.2.0-Linux-x86_64.sh -b -p /root/anaconda3 \
#     && echo "export PATH=/root/anaconda3/bin:$PATH" >> ~/.bashrc \
#     && bash -c "source /root/.bashrc"

RUN wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda3.sh
RUN bash ~/anaconda3.sh -b -p /home/anaconda3 \
	&& rm ~/anaconda3.sh 
ENV PATH /home/anaconda3/bin:$PATH

# RUN conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ \
#     && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/ \
#     && conda config --set show_channel_urls yes
# 不要用清华镜像，中科大镜像不错

RUN apt-get install -y python-qt4
RUN conda install -c jjhelmus tensorflow
RUN conda install -c conda-forge keras
RUN conda install -c menpo opencv 

