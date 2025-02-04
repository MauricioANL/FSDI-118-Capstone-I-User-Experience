from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola, mundo desde Django!")

# Create your views here.
