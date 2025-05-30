FROM python:3.6-slim

RUN mkdir -p /opt/calc

WORKDIR /opt/calc

COPY requires ./
RUN pip install --upgrade pytest>=6.0
RUN pip install -r requires
