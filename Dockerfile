FROM python:3.12-slim

RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /usr/apps/talent-application

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN apt-get clean
