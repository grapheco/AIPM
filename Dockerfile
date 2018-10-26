FROM tensorflow/tensorflow:1.5.0-py3

MAINTAINER airzihao

RUN apt update
RUN apt-get install wget
RUN cd /home \
    && wget --quiet https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh
RUN bash /home/Anaconda3-5.2.0-Linux-x86_64.sh -b -p /root/anaconda3 \
    && echo "export PATH=/root/anaconda3/bin:$PATH" >> ~/.bashrc \
    && bash -c "source /root/.bashrc"

EXPOSE 8888
