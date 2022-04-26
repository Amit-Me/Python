import speech_recognition as sr

start = sr.Recognizer()                     # Initialize the recognizer
sourse = sr.Microphone()
while(1):
	start.adjust_for_ambient_noise(sourse, duration=0.2)
	audio2 = start.listen(sourse)
	MyText = start.recognize_google(audio2)																	