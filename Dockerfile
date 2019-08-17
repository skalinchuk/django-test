# Pull the base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# Install MySQL
RUN apt-get update; apt-get install netcat python3-dev default-libmysqlclient-dev  -y

# Upgrade pip
RUN pip install pip -U
ADD requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt
ADD . /code/