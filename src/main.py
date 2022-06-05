# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/echoname/{name}")
async def echo(name:str):
    return f"Hello {name}"
