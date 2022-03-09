import speech_recognition as sr 
rec_vocale = sr.Recognizer()
mic = sr.Microphone()
with mic as src:
     audio = rec_vocale.listen(src)
     texte= rec_vocale.recognize_google(audio, language="en-US")
     aud = print(texte)
     