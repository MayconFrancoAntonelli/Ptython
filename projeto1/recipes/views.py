from django.http import HttpResponse
from django.shortcuts import render


def contato(request):
    return HttpResponse('contato')

def home(request):
    return HttpResponse('home')