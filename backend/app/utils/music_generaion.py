import os
import random
import shutil
import time
from pathlib import Path

from sqlalchemy.exc import InvalidRequestError

from app.data.schemas.SampleSchema import SampleCreateRequestSchema, SampleCreateSchema

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


async def create_samples(preset_id: int, sample_req: SampleCreateRequestSchema):
    if sample_req.text_request not in generation_dct:
        raise NotImplementedError(f"The sample request {sample_req.text_request} was not found.")

    res = []
    for sample_num in range(sample_req.count):
        rnd_file = get_random_file_from_dir(generation_dct[sample_req.text_request])
        new_file_name = f"{int(time.time_ns())}.wav"
        shutil.copy(rnd_file, static_place / new_file_name)

        new_sample_obj = {
            "name": f"{sample_req.text_request}",
            "preset_id": preset_id,
            "music_url": new_file_name
        }


        res.append(SampleCreateSchema.model_validate(new_sample_obj))

    return res


if __name__ == '__main__':
    print(music_place)