FROM python:3.11.1

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y 
RUN apt-get install postgresql gcc python3-dev musl-dev -y

RUN pip3 install --upgrade pip
COPY ./requirements/requirements-dev.txt .
RUN pip3 install -r requirements-dev.txt

COPY . /usr/src/app/