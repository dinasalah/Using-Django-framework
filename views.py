from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from datetime import datetime, timedelta

now = datetime.now() - timedelta(10)
mydate = now.strftime("%Y-%m-%dT%H:%M:%SZ") 

url = 'https://api.github.com/search/repositories?q=created:>' + mydate + '&sort=stars&order=desc&page=1&per_page=3'
resp = requests.get(url)
parsedResp = resp.json()
items = parsedResp["items"]

for item in items:
	print("********************************************")
	print(item['language'])
	try:
		langUrl = 'https://api.github.com/search/repositories?q=language:'+ item['language'] +'&order=desc'
		langResp= requests.get(langUrl)
		langParsedResp = langResp.json()
		print("Total Repositories count: ")
		print(langParsedResp["total_count"])

	except:
		print("Error in dealing with this language")
		continue
print("********************************************")
	
def index(request):
    return HttpResponse("Hello, world. You're at the polls indsfdsfdex.")
	
