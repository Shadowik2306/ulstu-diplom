import numpy as np
import sounddevice as sd
import soundfile as sf
from scipy.fft import rfft, rfftfreq


# def process_chunk(chunk, sample_rate):
#     # Example of frequency processing for each chunk
#     freqs = rfftfreq(len(chunk), d=1 / sample_rate)
#     fft_magnitudes = np.abs(rfft(chunk))
#
#     # Display top frequencies for the current chunk
#     if fft_magnitudes.size > 0:
#         top_indices = fft_magnitudes.argsort()[-3:][::-1]  # Top 3 magnitudes
#         top_frequencies = freqs[top_indices]
#         print(f"Top Frequencies: {top_frequencies}")
#     else:
#         top_frequencies = []
#
#     return chunk
#
#
# def play_audio_with_overlap(filename, chunk_size=1024, overlap=512):
#     # Open audio file
#     with sf.SoundFile(filename, 'r') as file:
#         sample_rate = file.samplerate
#         print(f"Sample rate: {sample_rate}, Channels: {file.channels}")
#
#         # Initial read position
#         hop_size = chunk_size - overlap
#         max_position = len(file) - chunk_size
#         start_position = 0
#
#         while start_position <= max_position:
#             # Move to correct start position
#             file.seek(start_position)
#             chunk = file.read(chunk_size, dtype='float32')
#
#             # If there's no more data, break
#             if len(chunk) == 0:
#                 break
#
#             # Process and play the chunk
#             processed_chunk = process_chunk(chunk, sample_rate)
#
#             sd.play(processed_chunk, samplerate=sample_rate)
#             sd.wait()  # Wait until the chunk is played
#
#
#             # Move to the next overlapping chunk
#             start_position += hop_size


class SoundEngine:
    __instance = None
    def __init__(self):
        self.dict = {

        }
        self.samples = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add_sample(self, data, id):
        self.dict[id] = [len(self.samples), 0, len(data)]
        self.samples.append(data)

    def __callback(self, outdata, frames, time, status):
        if status:
            print(status)


        res = np.zeros((14, ), dtype=np.float32)
        keys = dict(self.dict).keys()
        for sample_keys in keys:
            id_object, cur_id, size = self.dict[sample_keys]

            if cur_id >= size:
                continue

            res += self.samples[id_object][cur_id % size]
            self.dict[sample_keys][1] += 1

        print(res)
        outdata[:frames] = res[:, np.newaxis]


    def main_cycle(self):
        with sd.OutputStream(callback=self.__callback, samplerate=16000, channels=1):
            while True:
                sd.sleep(4)




# audio_signal = 0.5 * np.sin(2 * np.pi * 16000 * 5)
# print(audio_signal)
#
#
# # Example usage
#
#
# se = SoundEngine()
#
# se.add_sample('test1.wav')
# # se.add_sample('test2.wav')
# se.main_cycle()




# play_audio_with_overlap(filename, chunk_size=1024, overlap=512)
