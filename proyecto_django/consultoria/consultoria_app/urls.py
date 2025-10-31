from django.urls import path
from consultoria_app import views

urlpatterns = [
    
    path('', views.inicio, name='inicio'),
    path('contacto/', views.formulario_contacto, name='contacto'),
    path('DiagnosticoRapido/', views.formulario_diagnostico_rapido, name='DiagnosticoRapido'),
    path('AñadirProyecto/', views.formulario_añadir_trabajador, name='AñadirProyecto'),
    path('lista_proyectos/',views.view_lista_proyectos, name='lista_proyectos')
]

