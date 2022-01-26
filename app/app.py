from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {
        "name": "Image Database api",
        "docs": "/docs"
    }