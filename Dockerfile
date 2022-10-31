FROM python:3.10.4
RUN pip install "fastapi[all]"
RUN /usr/local/bin/python -m pip install --upgrade pip
EXPOSE 8080
