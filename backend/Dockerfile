FROM ubuntu:24.04
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt --break-system-packages