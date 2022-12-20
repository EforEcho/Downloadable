import wave
import struct
from math import sin, pi


audio = []
sample_rate = 44100.0

def append_sinewave(
    audio,
    freq=440.0,
    duration_millis=1000.0,
    volume=1.0):

    num_samples = duration_millis * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append (volume * sin(2 * pi * freq * (x / sample_rate)))

    return audio

def save_wav(audio, file_name):
    wav_file = wave.open(file_name, "w")
    nchannels = 1
    sampwidth = 2

    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    for sample in audio:
        wav_file.writeframes(struct.pack('h', int(sample * 32767)))

    wav_file.close()

def main(audio):
    audio = append_sinewave(audio)
    save_wav(audio, "main.wav")

if __name__ == "__main__":
    main(audio)