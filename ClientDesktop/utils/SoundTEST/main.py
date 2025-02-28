# import numpy as np
# import sounddevice as sd
#
# def generate_sine_wave(freq, duration, sample_rate=44100):
#     """Generate a sine wave of a given frequency and duration."""
#     t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Time vector
#     wave = 0.5 * np.sin(2 * np.pi * freq * t)  # Sine wave formula
#     return wave
#
# def main():
#     try:
#         # Get the frequency input from the user
#         freq = float(input("Enter the frequency in Hz (e.g., 440 for A4): "))
#         duration = 2  # Play sound for 2 seconds
#
#         # Generate the sine wave
#         sound_wave = generate_sine_wave(freq, duration)
#
#         # Play the sound
#         print(f"Playing {freq} Hz sound for {duration} seconds...")
#         sd.play(sound_wave, samplerate=44100)
#         sd.wait()  # Wait until the sound has finished playing
#
#         print("Playback finished.")
#
#     except ValueError:
#         print("Invalid input! Please enter a numeric frequency in Hz.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     main()
