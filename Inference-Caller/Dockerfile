FROM python:3.6
ADD /. /
WORKDIR /
#RUN apt-get update && yes | apt-get upgrade
#RUN apt-get install -y python3-pip
ADD requirements.txt /
RUN pip3 install -r requirements.txt