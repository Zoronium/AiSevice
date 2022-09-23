FROM python:3.10-slim

# RUN apk upgrade

WORKDIR /app
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies

# install python dependencies
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /app/
