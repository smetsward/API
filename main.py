from fastapi import FastAPI

app = FastAPI()


@app.get("/message")
async def root():
    return {"message": "hello world"}
