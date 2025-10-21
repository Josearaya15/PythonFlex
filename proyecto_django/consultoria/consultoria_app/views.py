from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def formulario_contacto(request):
    
    if request.method == 'POST':
        form = form_formulario_contacto(request.POST)

        if form.is_valid():
            form.save()
        return redirect('inicio')
    else:
        form = form_formulario_contacto()
    return render(request,'contacto.html', {'form': form})


def formulario_diagnostico_rapido(request):
    
    if request.method == 'POST':
        form = form_formulario_diagnostico_rapido(request.POST)

        if form.is_valid():
            form.save()
        return redirect('contacto')
    else:
        form = form_formulario_diagnostico_rapido()
    return render(request,'index.html', {'form': form})


def formulario_añadir_trabajador(request):
    
    if request.method == 'POST':
        form = form_formulario_añadir_proyecto(request.POST)

        if form.is_valid():
            form.save()
        return redirect('contacto')
    else:
        form = form_formulario_añadir_proyecto()
    return render(request,'index.html', {'form': form})


def view_lista_proyectos(request):
    query = request.GET.get('q','')
    if len(query) > 0:
        proyecto = Proyecto.objects.filter(
            nombre__icontains=query).order_by("nombre")
        
    else:
        proyecto = Proyecto.objects.all().order_by("nombre")
    
    return render(request, 'consultoria_app/lista_proyectos.html', {'proyecto': proyecto, 'query': query})
