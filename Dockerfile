FROM python:3.12.2-alpine3.19

ARG TOKEN
ARG CHANNEL_URL
ENV TOKEN $TOKEN
ENV CHANNEL_URL $CHANNEL_URL


COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]