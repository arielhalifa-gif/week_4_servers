from fastapi import FastAPI, HTTPException
from caesar import Caesar
from RailFence import RailFence
import uvicorn

app = FastAPI()

@app.get("/test/")
def say_hello():
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def call_name(name: str):
    with open("names.txt", "a") as f:
        f.write(name)
    return {"msg": "saved user"}

@app.post("/caesar/encrypt")
def encrypting_text(text: str, offset: int, mode):
    if mode == "encrypt":
        encrypted = Caesar.caesar_cipher_encryption(text, offset)
        return {"encrypted text": encrypted}
    elif mode == "decrypt":
        decrypted = Caesar.caesar_cipher_decryption(text, offset)
    body_dict = {"text": text, "offset": offset, "mode": mode}
    return {"decrypted text": decrypted}

@app.get("/fence/encrypt/{text}")
def encryption_text_by_fence(text: str):
    encrypted = RailFence.rail_fence_encryption(text)
    return {"encrypted": encrypted}

@app.post("/fence/decrypt")
def decryption_text_by_fence(text: str):
    decrypted = RailFence.rail_fence_decryption(text)
    return {"decrypted": decrypted}