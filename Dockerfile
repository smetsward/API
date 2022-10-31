FROM python:3.8

RUN pip install --upgrade -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "8080"]