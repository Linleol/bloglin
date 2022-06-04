from django.shortcuts import render
from django.http import HttpResponse
import datetime
def index(request):
	html ="<h2>Django專題Hello</h2><hr>"
	now = datetime.datetime.now()
	html = html + "現在時間:"+str(now)
	return HttpResponse(html)
def showdate(request):
	now = datetime.datetime.now()
	return HttpResponse("現在時間:"+str(now))