import wave
from array import array

import numpy as np
from diffusers import AudioLDM2Pipeline
import scipy
import torch


class AudioLDM2Generator:
    def __init__(self, model_name="cvssp/audioldm2"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.pipeline = AudioLDM2Pipeline.from_pretrained(model_name)
        self.pipeline.to(self.device)

    def generate_audio(self, prompt, num_samples=1, output_path="output.wav"):
        for i in range(num_samples):
            result = self.pipeline(
                prompt=prompt,
                audio_length_in_s=5.0,
                num_inference_steps=50,

            ).audios[0]

            rate = 16000
            output_file = f"{output_path.split('.')[0]}_{i}.wav"

            scipy.io.wavfile.write(output_file, rate, data=result)


if __name__ == "__main__":
    ldm_model = AudioLDM2Generator()
    ldm_model.generate_audio("City sound")