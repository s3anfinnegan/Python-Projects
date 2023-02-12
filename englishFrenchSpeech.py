import pyaudio
import keyboard
import wave
import time
import speech_recognition as sr
from translate import Translator
from gtts import gTTS
import pygame


#Step 1: Create .wav file 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

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

#timestamp = str(int(time.time()))
filename = "audioEN.wav"

wf = wave.open(filename, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

#Step 2: Use Google STT to create .txt file 
def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)


text = transcribe_audio(filename)

with open("english.txt", "w") as file:
    file.write(text)

#Step 3: Translate text from English to French
with open('english.txt', mode='r') as file:
    text = file.read()

translator = Translator(to_lang="fr")
translation = translator.translate(text)

with open('french.txt', mode='w') as file:
    file.write(translation)

#Step 4: Create French .wav file
with open("french.txt", "r") as file:
    text = file.read()

tts = gTTS(text, lang='fr')
tts.save("audioFR.wav")
