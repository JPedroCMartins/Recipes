from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'João Pedro',
    })

def contato(request):
    return HttpResponse("Contato")

def sobre(request):
    return HttpResponse("Sobre")