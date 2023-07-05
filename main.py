from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hello root"


@app.get("/hello/{name}")
async def say_hello():
    return "Hello"

