from dataclasses import dataclass

import numpy as np
import sounddevice as sd

@dataclass
class MidiChannelPreferences:
    volume: int


class SoundEngine:
    _instance = None

    def __init__(self):
        self.dict = {}
        self.midi_channels_preferences: dict[MidiChannelPreferences] = {}
        self.samples = []

    def add_midi_channel_configuration(self, midi_id, volume):
        if midi_id in self.midi_channels_preferences:
            print(f"Midi channel with id {midi_id} already exists")
            return
        self.midi_channels_preferences[midi_id] = MidiChannelPreferences(
            volume=volume
        )

    def change_midi_channel_volume(self, midi_id, volume):
        if midi_id not in self.midi_channels_preferences:
            print(f"Midi channel with id {midi_id} does not exist")
            return
        print(f"Midi channel {midi_id} volume {volume} changed")
        self.midi_channels_preferences[midi_id].volume = volume

    def add_sample(self, data, midi_channel_id, channel):
        self.dict[(midi_channel_id, channel)] = [len(self.samples), 0, len(data)]
        self.samples.append(data)

    def __callback(self, outdata, frames, time, status):
        if status:
            print(status)

        res = np.zeros((14, ), dtype=np.float32)
        keys = dict(self.dict).keys()
        for sample_keys in keys:
            id_object, cur_id, size = self.dict[sample_keys]
            volume = self.midi_channels_preferences[sample_keys[0]].volume / 100

            if cur_id >= size:
                del self.dict[sample_keys]
                del self.samples[id_object]
                continue

            res += self.samples[id_object][cur_id % size] * volume
            self.dict[sample_keys][1] += 1

        outdata[:frames] = res[:, np.newaxis]

    def main_cycle(self):
        with sd.OutputStream(callback=self.__callback, samplerate=16000, channels=1):
            while True:
                sd.sleep(4)


def sound_engine_singleton_factory(_singleton= SoundEngine()):
    return _singleton






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
