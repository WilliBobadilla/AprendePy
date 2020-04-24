from django.db import models

# Create your models here.


class Autor(models.Model):
    nombreAutor = models.CharField(max_length=60)
    correo = models.EmailField(null=True, blank=True) #para que sea un campo opcional
    github = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.nombreAutor



class Curso(models.Model):
    nombreCurso = models.CharField(max_length=50)
    #fechaPublicacion = models.DateField(auto_now_add=True)
    descripcionCurso = models.TextField(null=True, blank=True,default="No hay descripcion")
    autor = models.ManyToManyField("Autor")
    link = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.nombreCurso
    

    

# class Unidad(models.Model):
#     nombreUnidad = models.CharField(max_length=100)
#     link = models.URLField(null=True, blank=True)    

#     def __str__(self):
#         return self.nombreUnidad
