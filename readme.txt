//
Homer Browser 0.1a
Prithviraj Jadhav - Vesuvio Systems
Copyright 2016
GPLv3  

Description: A simple implementation of a web browser for blind people
Problems: javascript based dynamic websites(angular,react,meteor,etc) will not work
//

Features:
{
	Bookmarking
	Set Homepage
	Say "skipline" to skip curr. line
	Say "skippara" to skip current para 
}

Program Flow{
	Startup{
		Speak-Put on headphones and mic
		Speak-opened homepage {{name}}
		SpeachRec-Bookmark or home page
		if Homepage -> parse speak homepage
	}
}

PageParser-TTS {
	
}	