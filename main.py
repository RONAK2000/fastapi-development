from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Sneha"}

@app.get("/Home")
async def root():
    return {"200":"Welcomr"}
