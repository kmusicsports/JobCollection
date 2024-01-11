FROM python:3.11

WORKDIR /project

COPY ./requirements.txt ./

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
