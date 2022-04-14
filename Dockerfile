FROM python:3.8-alpine
MAINTAINER Luisa Valderrama Developer

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


WORKDIR /swapi
COPY ./swapi /swapi

RUN adduser -D user
USER user