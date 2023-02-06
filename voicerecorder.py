#Building a recorder using pyaudio
#further functionality can translate to text

import pyaudio
import keyboard
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

counter = 1

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording... press 'q' to stop")

frames = []

while True:
    data = stream.read(CHUNK)
    frames.append(data)
    if keyboard.is_pressed('q'):
        break

stream.stop_stream()
stream.close()
p.terminate()

print("Stopped recording")

filename = "output_" + str(counter) + ".wav"
counter += 1

wf = wave.open(filename, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()




