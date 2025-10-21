from django.db import models

# Create your models here.
#Modelos son los manipuladores de data
class Empresas(models.Model):
    nombre_empresa=models.CharField(max_length=100)
    rubro=models.CharField(max_length=100)
    tamaño=models.CharField(max_length=50)
    identificador=models.CharField(max_length=20)
    email_asociado=models.EmailField()
    fecha_creacion=models.DateField(auto_now_add=True) 

    def __str__(self):
        return f'{self.nombre_empresa}, rubro:{self.rubro}'
    
class DiagnosticoRapido(models.Model):
    industria=models.CharField(max_length=100)
    trabajadores=models.IntegerField()
    prioridad=models.CharField(max_length=100)
    email_asociado=models.EmailField()
    fecha_creacion=models.DateField(auto_now_add=True) 

    def __str__(self):
        return f'{self.industria},trabajadores:{self.trabajadores},prioridad:{self.prioridad}'
    

class Proyecto(models.Model):
    nombre=models.CharField(max_length=100)
    tema=models.CharField(max_length=100)
    area_empresa=models.CharField(max_length=100)
    duracion=models.CharField(max_length=100)
    presupuesto=models.IntegerField()

    def __str__(self):
        return f'{self.nombre}, tema: {self.tema}'