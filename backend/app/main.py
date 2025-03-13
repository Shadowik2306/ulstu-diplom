from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

from app.data.repositories.MusicRepository import MusicRepository
from app.data.repositories.NoteRepository import NoteRepository
from app.routers.file_router import router as file_router
from app.routers.preset_router import presets_router, preset_router
from app.routers.samples_router import router as samples_router
from app.routers.auth_router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await NoteRepository.initialize_table()
    yield


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(file_router)
app.include_router(preset_router)
app.include_router(presets_router)
app.include_router(samples_router)
app.include_router(auth_router)


@app.get("/")
async def main(request: Request):
    return {"message": "Hello World"}







