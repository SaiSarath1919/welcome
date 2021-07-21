from gtts import gTTS
from playsound import playsound
output = 'output_audio.mp3'
language = 'en'
text_to_convert = "ela vunav"
sp = gTTS(text_to_convert,lang = language,slow = False)
sp.save(output)
playsound(output)
print("Hello")
