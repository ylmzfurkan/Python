from gtts import gTTS
import os

def text_to_speech(text, lang='tr'):
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("speech.mp3")
    os.system("mpg123 speech.mp3")

with open('kitap-seslendirme/kitap.txt', 'r') as file:
    text = file.read().replace('\n', ' ')

text_to_speech(text)
