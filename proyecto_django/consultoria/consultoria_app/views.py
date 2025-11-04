from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def formulario_contacto(request):
    
    if request.method == 'POST':
        form = form_formulario_contacto(request.POST)

        if form.is_valid():
            form.save()
        return redirect('consultoria_app:inicio')
    else:
        form = form_formulario_contacto()
    return render(request,'contacto.html', {'form': form})


def formulario_diagnostico_rapido(request):
    
    if request.method == 'POST':
        form = form_formulario_diagnostico_rapido(request.POST)

        if form.is_valid():
            form.save()
        return redirect('consultoria_app:contacto')
    else:
        form = form_formulario_diagnostico_rapido()
    return render(request,'index.html', {'form': form})

@login_required
def formulario_añadir_proyecto(request):
    
    if request.method == 'POST':
        form = form_formulario_añadir_proyecto(request.POST)

        if form.is_valid():
            form.save()
        return redirect('consultoria_app:lista_proyectos')
    else:
        form = form_formulario_añadir_proyecto()
    return render(request,'consultoria_app/AñadirProyecto.html', {'form': form})

@login_required
def view_lista_proyectos(request):
    query = request.GET.get('q')
    if query:
        proyectos = Proyecto.objects.filter(nombre__icontains=query)
    else:
        proyectos = Proyecto.objects.all()

    if request.method == 'POST':
        # Eliminar proyecto
        if 'eliminar' in request.POST:
            proyecto_id = request.POST.get('eliminar')
            proyecto = get_object_or_404(Proyecto, id=proyecto_id)
            proyecto.delete()
            return redirect('consultoria_app:lista_proyectos')

        # Editar proyecto
        elif 'editar' in request.POST:
            proyecto_id = request.POST.get('editar')
            proyecto = get_object_or_404(Proyecto, id=proyecto_id)

            proyecto.tema = request.POST.get('tema')
            proyecto.area_empresa = request.POST.get('area_empresa')
            proyecto.duracion = request.POST.get('duracion')
            proyecto.presupuesto = request.POST.get('presupuesto')
            proyecto.save()

            return redirect('consultoria_app:lista_proyectos')

    contexto = {
        'proyecto': proyectos,
        'query': query,
    }

    return render(request, 'consultoria_app/lista_proyectos.html', contexto)