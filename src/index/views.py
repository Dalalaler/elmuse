from platform import system
from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import render



def elmuse(request):
    return render(request, "index/elmuse.html",)

# Create your views here.
