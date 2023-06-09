FROM python:3.10.9-slim-buster
LABEL maintainer="kabatova.anna@ukr.net"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . .
