import html_engine as wbp
import speech_core as spc

page=wbp.parse_webpage("sample.html")
spc.initAndSpeak(page['body'])