from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>Agora é %s.</body></html>" % now        
    return HttpResponse(html)
    