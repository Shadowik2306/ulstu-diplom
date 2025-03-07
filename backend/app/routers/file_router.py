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


def create_file(file: UploadFile):
    try:
        file_location = STATIC_PATH / file.filename
        with open(file_location, "wb+") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"info": f"File '{file.filename}' saved at '{file_location}'"}
    except Exception as e:
        print(str(e))
        return {"message": "File download failed", "error": str(e)}


@router.get("")
async def get_files():
    return [file.name for file in STATIC_PATH.iterdir() if file.is_file()]


@router.get("/{file_name}")
async def get_file_by_name(file_name: str):
    file_path = STATIC_PATH / file_name
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")