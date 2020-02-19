FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-c"]

RUN set -x && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    wget \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    git \
    curl \
    locales \
    language-pack-ja-base \
    language-pack-ja \
    vim

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE "C.UTF-8"

# set timezone
RUN sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.jaist.ac.jp/pub/Linux/ubuntu/%g" /etc/apt/sources.list

ENV TZ Asia/Tokyo
RUN apt-get install -y tzdata && \
    rm -rf /var/lib/apt/lists/* && \
    echo "${TZ}" > /etc/timezone && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && \
    apt-get install -y libgmp3-dev

WORKDIR /home/project
COPY Pipfile* /home/project/

RUN pip3 install pipenv
RUN pipenv sync

CMD ["/usr/bin/tail", "-f", "/dev/null" ]
