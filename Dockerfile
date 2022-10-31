FROM python:3.10.0-alpine
WORKDIR /app
COPY ./app api/app
EXPOSE 8000