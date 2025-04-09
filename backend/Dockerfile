FROM ubuntu:24.04
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt --break-system-packages

COPY ./app/setup_audio_ldm.py /app/setup_audio_ldm.py
RUN python /app/setup_audio_ldm.py

COPY ./app /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]