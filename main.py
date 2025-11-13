from fastapi import FastAPI, HTTPException
from caesar import Caesar
from RailFence import RailFence
import uvicorn

app = FastAPI()

@app.get("/test/")
def say_hello():
    return f"hi from test"


@app.get("/test/{name}")
def call_name(name: str):
    with open("names.txt", "a") as f:
        f.write(name)
    return f"saved user"

