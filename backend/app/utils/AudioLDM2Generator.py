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
    pipeline = AudioLDM2Pipeline.from_pretrained("cvssp/audioldm2")
    pipeline.to(device)

    @classmethod
    def generate_audio(cls, prompt, num_samples=1):
        samples_name = []
        for i in range(num_samples):
            result = cls.pipeline(
                prompt=prompt,
                audio_length_in_s=2.0,
                num_inference_steps=50,
            ).audios[0]

            rate = 16000
            output_file = f"{int(time.time_ns())}.wav"

            scipy.io.wavfile.write(static_path / output_file, rate, data=result)
            samples_name.append(output_file)

        return samples_name

    @classmethod
    def create_samples(
        cls,
        sample_req: MusicCreateRequestSchema
    ):
        samples_name = cls.generate_audio(sample_req.text_request, num_samples=sample_req.count)
        return samples_name
