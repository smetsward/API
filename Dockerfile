FROM python:3.10.4
WORKDIR /app
COPY requirements.txt .
RUN pip install "fastapi[all]"
COPY . .
EXPOSE 8080
