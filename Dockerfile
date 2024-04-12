# pull official base image
FROM python:3.12.1-slim-bookworm

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#?install Netcat
RUN apt-get update \
    && apt-get -y install netcat-traditional gcc postgresql \
    && apt-get clean

# add app
COPY . .

#copy wait_for_postgres.sh
COPY ./wait_for_postgres.sh .
RUN sed -i 's/\r$//g' /usr/src/app/wait_for_postgres.sh
RUN chmod +x /usr/src/app/wait_for_postgres.sh
