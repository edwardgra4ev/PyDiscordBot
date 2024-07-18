FROM python:3.12
ENV PYTHONUNBUFFERED 1

RUN mkdir /discord_bot
WORKDIR /discord_bot

COPY requirements.txt /discord_bot
COPY main.py /discord_bot

RUN pip install -r requirements.txt