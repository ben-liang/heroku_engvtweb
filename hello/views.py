from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import requests
from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

