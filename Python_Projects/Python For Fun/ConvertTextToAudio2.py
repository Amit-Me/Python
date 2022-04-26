import pyttsx3

engine = pyttsx3.init()

text = input("Enter what you want to convert into speech \n")

engine.say(text)

engine.runAndWait()