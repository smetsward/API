from fastapi import FastAPI
from random import randint

app = FastAPI()


@app.get("/message")
async def root():
    return {"message": "hello"}