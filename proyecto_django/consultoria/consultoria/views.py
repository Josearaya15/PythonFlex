<<<<<<< HEAD
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader

def inicio(request):
=======
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader

def inicio(request):
>>>>>>> 88f5804 (carga inicial)
    return render(request, 'index.html')