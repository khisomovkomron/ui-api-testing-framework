FROM python:latest

MAINTAINER komronkhisomov@gmail.com

RUN apt-get update && apt-get -y install vim

RUN mkdir /automation

COPY ./threek_apitest /automation/threek_apitest
COPY ./setup.py /automation
COPY ./env.bat /automation

WORKDIR /automation

RUN python3 setup.py install