# The Broccoli core. Downloads webpage ,parses it 
# and returns reformatted text for speech_engine

import requests
from bs4 import BeautifulSoup

# tested working
def get_webpage(url):
	page = requests.get(url)
	if(page.status_code is not 200):
		return -1
	return str(page)


# remove scripts,images,
# tested working
def parse_webpage(webpage):
	soup = BeautifulSoup(open(webpage,'r'),'html.parser')
	page=[]
	img = soup.select('img')
	scripts=soup.select('script')
	body=str(soup.select('body')[0])
	
	for each in img:
		each=str(each)
		if each in body:
			pos=body.find(each)
			body=body[:pos]+body[pos+len(each):]

	for each in scripts:
		each=str(each)
		if each in body:
			pos=body.find(each)
			body=body[:pos]+body[pos+len(each):]
	bodySoup=BeautifulSoup(body,'html.parser')
	page={'title':soup.select('title')[0].text,'body':bodySoup.text}
	return page
	


