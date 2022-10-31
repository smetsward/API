FROM python:3.8

RUN pip install --upgrade

EXPOSE 8080

CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "8080"]