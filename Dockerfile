# version: 0.0.1
From ubuntu:18.04

MAINTAINER airzihao

RUN apt update
RUN apt-get install -y wget
RUN apt-get install -y vim

RUN wget https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda3.sh
RUN bash ~/anaconda3.sh -b -p /home/anaconda3 \
	&& rm ~/anaconda3.sh 
ENV PATH /home/anaconda3/bin:$PATH

RUN apt-get install -y python-qt4
RUN conda install -c conda-forge keras
RUN conda install -c menpo opencv
RUN conda install -c anaconda configparser
RUN conda install -c jjhelmus tensorflow

#pip install tensorflow==1.9.0
#RUN pip install keras
#RUN pip install opencv-python
#RUN pip install configparser

