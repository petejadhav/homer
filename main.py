import html_engine as wbp
import speech_core as spc
import threading

#listenThread=threading.Thread(target=speakThread)
#speakThread=threading.Thread(target=listenThread)

def speakThread():
	page=wbp.parse_webpage("sample.html")
	spc.initAndSpeak(page['body'])

def listenThread():
	words=spc.listen()
	#check word conditions