FROM python:3.12
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
COPY main.py /app

RUN pip install -r requirements.txt