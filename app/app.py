from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


from app.routes import router

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

@app.get("/")
def get_root():
    return {
        "name": "Image Database api",
        "docs": "/docs"
    }

app.include_router(router, prefix="")