from gtts import gTTS

text = " Hello guys. how are you. All good?"

language = 'en'

obj = gTTS(text = text, lang=language,slow = False)
obj.save("sample.mp3")