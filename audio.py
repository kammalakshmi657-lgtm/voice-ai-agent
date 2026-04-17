import sounddevice as sd
from scipy.io.wavfile import write
import uuid

def record_audio(duration=5, fs=44100):
    filename = f"recorded_{uuid.uuid4()}.wav"
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    return filename