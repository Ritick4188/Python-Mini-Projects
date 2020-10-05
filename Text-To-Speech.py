import pyttsx3

data = input('Enter Your Text To Speech : ')

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()