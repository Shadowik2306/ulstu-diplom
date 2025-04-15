import shutil
from pathlib import Path

from fastapi import APIRouter, HTTPException, File, UploadFile, Request
from fastapi.responses import FileResponse
import os

STATIC_PATH = Path(__file__).parent.parent.parent / "static"


router = APIRouter(
    prefix="/files",
    tags=["File"]
)



@router.get("/{file_name}")
async def get_file_by_name(file_name: str):
    file_path = STATIC_PATH / file_name
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")