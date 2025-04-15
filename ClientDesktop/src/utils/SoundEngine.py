import time as t

import numpy as np
import sounddevice as sd


class SoundEngine:
    def __init__(self):
        self.midi_channel_volumes = {}
        self.sound_state = {}
        # self.last = 0

    def add_midi_channel(self, midi_channel_id, volume):
        if midi_channel_id in self.midi_channel_volumes:
            print(f"MIDI channel {midi_channel_id} already added.")
        self.midi_channel_volumes[midi_channel_id] = volume

    def update_midi_channel(self, midi_channel_id, volume):
        if midi_channel_id not in self.midi_channel_volumes:
            print(f"MIDI channel {midi_channel_id} doesn't exist.")
        self.midi_channel_volumes[midi_channel_id] = volume

    def add_sound(self, midi_channel_id, note, data):
        if midi_channel_id not in self.midi_channel_volumes:
            print(f"No info about midi channel {midi_channel_id}")
            return
        if (midi_channel_id, note) in self.sound_state:
            return
        self.sound_state[(midi_channel_id, note)] = data

    def remove_sound(self, midi_channel_id, note):
        if (midi_channel_id, note) not in self.sound_state:
            return
        del self.sound_state[(midi_channel_id, note)]

    def callback(self, outdata, frames, time, status):
        if status:
            print(status)

        res = np.zeros((frames, ), dtype=np.float32)
        saved_sound_state_keys = dict(self.sound_state).keys()
        for key in saved_sound_state_keys:
            try:
                volume = self.midi_channel_volumes[key[0]] / 100
                state = self.sound_state[key][:frames] * volume
                if state.size == 0:
                    del self.sound_state[(key[0], key[1])]
                    continue
                padding = (0, frames - len(state))
                state = np.pad(state, padding, 'constant', constant_values=0)
                self.sound_state[key] = self.sound_state[key][frames:]
                res += state
            except StopIteration:
                del self.sound_state[(key[0], key[1])]
                continue

        outdata[:frames] = res[:, np.newaxis]


def sound_engine_singleton_factory(_object= SoundEngine()):
    return _object