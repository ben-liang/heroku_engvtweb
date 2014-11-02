from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'engvtweb/index.html', {})

def my_account(request):
    return render(request, 'engvtweb/my_account.html', {})
