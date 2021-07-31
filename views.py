from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from itertools import islice
from datetime import datetime, timedelta

now = datetime.now() - timedelta(10)
mydate = now.strftime("%Y-%m-%dT%H:%M:%SZ") 

url = 'https://api.github.com/search/repositories?q=created:>' + mydate + '&sort=stars&order=desc&page=1&per_page=3'
a = requests.get(url)
#print(a.status_code)
b = a.json()
c = b["items"]

for x in c:
	print("********************************************")
	print(x['language'])
	try:
		u = 'https://api.github.com/search/repositories?q=language:'+ x['language'] +'&order=desc'
		#print(u)
		l = requests.get(u)
		m = l.json()
		print("Total Repositories count: ")
		print(m["total_count"])

	except:
		print("Error in dealing with this language")
		continue
print("********************************************")
	
def index(request):
    return HttpResponse("Hello, world. You're at the polls indsfdsfdex.")
	