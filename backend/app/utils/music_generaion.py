import os
import random
import shutil
import time
from pathlib import Path
from fastapi import HTTPException
from sqlalchemy.exc import InvalidRequestError


from app.data.schemas.SampleSchema import SampleCreateSchema
from app.data.schemas.MusicSchema import MusicCreateRequestSchema, MusicCreateSchema

music_place = Path(__file__).parent.parent.parent / "music_buff"
static_place = Path(__file__).parent.parent.parent / "static"


generation_dct = {
    "piano": music_place / "piano",
    "guitar": music_place / "guitar"
}

def get_random_file_from_dir(directory_path):
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    except FileNotFoundError:
        print(f"The directory {directory_path} was not found.")
        return None
    except PermissionError:
        print(f"Permission denied for accessing {directory_path}.")
        return None

    # Check if there are any files
    if not files:
        print("No files found in the given directory.")
        return None

    # Select a random file from the list
    return directory_path / random.choice(files)


async def create_samples(
        preset_id: int,
        sample_req: MusicCreateRequestSchema
) -> list[SampleCreateSchema]:
    from app.data.repositories.MusicRepository import MusicRepository

    if sample_req.text_request not in generation_dct:
        raise HTTPException(
            status_code=501,
            detail=f"The sample request \"{sample_req.text_request}\" was not found."
        )

    res = []
    for sample_num in range(sample_req.count):
        rnd_file = get_random_file_from_dir(generation_dct[sample_req.text_request])
        new_file_name = f"{int(time.time_ns())}.wav"
        shutil.copy(rnd_file, static_place / new_file_name)

        music_model = await MusicRepository().create(MusicCreateSchema(
            music_url=f"{new_file_name}"
        ))

        res.append(SampleCreateSchema(
            name=f"{sample_req.text_request}",
            music_id=music_model.id,
            preset_id=preset_id,
        ))

    return res


async def delete_sample_file(sample_ulr: str):
    os.remove(static_place / sample_ulr)


if __name__ == '__main__':
    print(music_place)