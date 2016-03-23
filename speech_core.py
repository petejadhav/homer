import pyttsx as tts

def initAndSpeak(words):
	engine=tts.init()
	engine.say(words)
	engine.runAndWait()