from translate import Translator
from gtts import gTTS

#Translating the English .txt file into a French .txt file
#with additional functionality, we will be able to translate
#into a French .wav file (hopefully!)

with open('test.txt', mode='r') as file:
    text = file.read()

translator = Translator(to_lang="fr")
translation = translator.translate(text)

with open('french.txt', mode='w') as file:
    file.write(translation)


# Open the .txt file
with open("french.txt", "r") as file:
    text = file.read()

# Use gTTS to generate a .wav file from the text
tts = gTTS(text, lang='fr')
tts.save("audio.wav")
