import speech_recognition as sr
import time

#Simple application to transcribe .wav to .txt (Speech to Text application)

def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

filename = "output_1.wav"
text = transcribe_audio(filename)

timestamp = str(int(time.time()))
with open("transcription_" + timestamp + ".txt", "w") as file:
    file.write(text)
