FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python3.4 python3-pip libpq-dev python3.4-dev libxml2-dev libxslt1-dev python3-dev git
ADD requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /code
