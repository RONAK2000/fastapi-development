from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Mehul"}

@app.get("/Home")
async def root():
    return {"200":"Welcomr"}
