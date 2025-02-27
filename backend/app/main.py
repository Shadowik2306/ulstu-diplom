from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from pathlib import Path

from app.routers.file_router import router as file_router
from app.routers.preset_router import router as preset_router


app = FastAPI()
app.include_router(file_router)
app.include_router(preset_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
