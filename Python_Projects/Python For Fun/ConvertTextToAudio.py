from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'hi'
sp = gTTS("Enter Your name",lang = language,slow=False)

sp.save(audio)
playsound("speech.mp3")