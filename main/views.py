from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import socket
from .forms import *
from .Location import jva
from .templates.main import map

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
# Create your views here.

def index(response):
    return render(response,"main/index.html",{})

def entrypage(response):
    #print(jva.getLocation())
    if response.method=="POST":
        form=GetEntry(response.POST)
        if form.is_valid():
            n=form.cleaned_data["name"]
            p=form.cleaned_data["phoneNo"]
            s=form.cleaned_data["status"]
            info=Information(name=n,phoneNo=p,status=s,ip=ip_address,location=str(jva.getLocation()))
            info.save()
    else:
        form=GetEntry()

    return render(response,"main/entry.html",{'form':form})

def demopage(response):
    
    return render(response,"main/map.html",{})
