import pyttsx as tts
import speech_recognition as rec


		

	def speak(words):
		engine=tts.init()
		engine.say(words)
		engine.runAndWait()

	def listen():
		#call recognizer and return string
		return strng
