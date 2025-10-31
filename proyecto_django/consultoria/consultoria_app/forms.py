from django import forms
from consultoria_app.models import *

class form_formulario_contacto(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['nombre_empresa','rubro','tamaño','identificador','email_asociado']
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'rubro': forms.TextInput(attrs={'class': 'form-control'}),
            'tamano': forms.Select(choices=[
                ('Pequeña', 'Pequeña'),
                ('Mediana', 'Mediana'),
                ('Grande', 'Grande')
            ], attrs={'class': 'form-control'}),
            'identificador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12.345.678-9'}),
            'email_asociado': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'empresa@dominio.cl'}),
        }

class form_formulario_diagnostico_rapido(forms.ModelForm):
    class Meta:
        model = DiagnosticoRapido
        fields = ['industria','trabajadores','email_asociado','prioridad']
        widgets = {
            'industria': forms.TextInput(attrs={'class': 'form-control'}),
            'trabajadores': forms.NumberInput(attrs={'class': 'form-control'}),
            'prioridad': forms.Select(choices=[
                ('Reducir costos', 'Reducir costos'),
                ('Automatizar procesos', 'Automatizar procesos'),
                ('Transformación digital', 'Transformación digital')
            ], attrs={'class': 'form-control'}),
            'email_asociado': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'empresa@dominio.cl'}),
        }

class form_formulario_añadir_proyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre','tema','area_empresa','duracion','presupuesto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tema': forms.TextInput(attrs={'class': 'form-control'}),
            'area_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.Select(choices=[
                ('Corto', 'Corto'),
                ('Medio', 'Medio'),
                ('Largo', 'Largo')
            ], attrs={'class': 'form-control'}),
            'presupuesto': forms.NumberInput(attrs={'class': 'form-control'}),

        }
