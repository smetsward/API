FROM python:3.10.0-alpine
WORKDIR /code
EXPOSE 8080
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY main.py /code/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
