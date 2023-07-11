FROM python:3.8-slim


RUN apt-get update

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

WORKDIR /app


