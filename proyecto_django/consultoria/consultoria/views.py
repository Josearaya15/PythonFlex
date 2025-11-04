from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader

def inicio(request):
    return render(request, 'index.html')

def AcercaDeMi(request):
    return render(request, 'AcercaDeMi.html')