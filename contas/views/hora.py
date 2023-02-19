from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def agora(request):
    agora = datetime.datetime.now()
    html = "<html><body>Agora é %s.</body></html>" % now
    return HttpResponse(agora)
    