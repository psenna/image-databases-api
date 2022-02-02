from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routes import router
from app.config.database import database
app = FastAPI()

@app.on_event("startup")
async def startup() -> None:
     if not database.is_connected:
        await database.connect()
        return


@app.on_event("shutdown")
async def shutdown() -> None:
    if database.is_connected:
        await database.disconnect()

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