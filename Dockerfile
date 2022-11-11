FROM python:3.10.0-alpine
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./myproject/ /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


#FROM python:3.10.0-slim
#WORKDIR /code
#EXPOSE 8000
#COPY ./requirements.txt /code/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#COPY ./myproject /code
#RUN mkdir -p /code/sqlitedb
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

