import time
import wave
from array import array
from pathlib import Path

from diffusers import AudioLDM2Pipeline
import scipy
import torch

from app.data.schemas.MusicSchema import MusicCreateRequestSchema, MusicCreateSchema
from app.data.schemas.SampleSchema import SampleCreateSchema

static_path = Path(__file__).parent.parent.parent / "static"


class AudioLDM2Generator:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if torch.cuda.is_available():
        pipeline = AudioLDM2Pipeline.from_pretrained("cvssp/audioldm2", torch_dtype=torch.float16)
    else:
        pipeline = AudioLDM2Pipeline.from_pretrained("cvssp/audioldm2")
    pipeline.to(device)

    @classmethod
    def generate_audio(cls, sample_req: MusicCreateRequestSchema):
        result = cls.pipeline(
            prompt=sample_req.count,
            negative_prompt=sample_req.negative_prompt,
            audio_length_in_s=sample_req.audio_length_in_s,
            num_inference_steps=sample_req.num_inference_steps,
            num_waveforms_per_prompt=sample_req.num_waveforms_per_prompt,
        ).audios[0]

        rate = 16000
        output_file = f"{int(time.time_ns())}.wav"

        scipy.io.wavfile.write(static_path / output_file, rate, data=result)

        return output_file