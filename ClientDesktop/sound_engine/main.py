import numpy as np
import sounddevice as sd
import soundfile as sf
from scipy.fft import rfft, rfftfreq


def process_chunk(chunk, sample_rate):
    # Example of frequency processing for each chunk
    freqs = rfftfreq(len(chunk), d=1 / sample_rate)
    fft_magnitudes = np.abs(rfft(chunk))

    # Display top frequencies for the current chunk
    if fft_magnitudes.size > 0:
        top_indices = fft_magnitudes.argsort()[-3:][::-1]  # Top 3 magnitudes
        top_frequencies = freqs[top_indices]
        print(f"Top Frequencies: {top_frequencies}")
    else:
        top_frequencies = []

    return chunk


def play_audio_with_overlap(filename, chunk_size=1024, overlap=512):
    # Open audio file
    with sf.SoundFile(filename, 'r') as file:
        sample_rate = file.samplerate
        print(f"Sample rate: {sample_rate}, Channels: {file.channels}")

        # Initial read position
        hop_size = chunk_size - overlap
        max_position = len(file) - chunk_size
        start_position = 0

        while start_position <= max_position:
            # Move to correct start position
            file.seek(start_position)
            chunk = file.read(chunk_size, dtype='float32')

            # If there's no more data, break
            if len(chunk) == 0:
                break

            # Process and play the chunk
            processed_chunk = process_chunk(chunk, sample_rate)

            sd.play(processed_chunk, samplerate=sample_rate)
            sd.wait()  # Wait until the chunk is played


            # Move to the next overlapping chunk
            start_position += hop_size



class SoundEngine:
    def __init__(self):
        self.dict = {

        }
        self.samples = []


    def add_sample(self, sample_file_name, id=0):
        file = sf.SoundFile(sample_file_name,)
        if file.samplerate != 16000:
            print("NOT IMPLEMENTED OTHER RATE")
            return None

        file_freq = sf.read(sample_file_name, dtype='float32')[0]
        chunk_size = 14
        num_chunks = len(file_freq) // chunk_size + (len(file_freq) % chunk_size != 0)
        self.dict[len(self.dict.keys())] = [len(self.samples), 0, num_chunks]
        chunks = np.array_split(file_freq, num_chunks)
        for i in range(len(chunks)):
            if len(chunks[i]) < chunk_size:
                chunks[i] = np.pad(chunks[i], (0, chunk_size - len(chunks[i])), 'constant', constant_values=0)
        self.samples.append(chunks)

    def __callback(self, outdata, frames, time, status):
        if status:
            print(status)

        res = np.zeros(14, dtype=np.float32)
        for sample_keys in self.dict.keys():
            id_object, cur_id, size = self.dict[sample_keys]

            # if cur_id >= size:
            #     continue
            res += self.samples[id_object][cur_id % size]
            self.dict[sample_keys][1] += 1

        outdata[:frames] = res[:, np.newaxis]


    def main_cycle(self):
        i = 0
        with sd.OutputStream(callback=self.__callback, samplerate=16000, channels=1):
            while True:
                sd.sleep(10)



audio_signal = 0.5 * np.sin(2 * np.pi * 16000 * 5)
print(audio_signal)


# Example usage


se = SoundEngine()

se.add_sample('test1.wav')
se.add_sample('test2.wav')
se.main_cycle()




# play_audio_with_overlap(filename, chunk_size=1024, overlap=512)
