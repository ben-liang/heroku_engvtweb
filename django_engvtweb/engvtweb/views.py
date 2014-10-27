from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'engvtweb/index.html', {})