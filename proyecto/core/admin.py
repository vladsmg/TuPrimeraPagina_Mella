from django.contrib import admin

from . import models

admin.site.register(models.Curso)
admin.site.register(models.CursoEstudiante)
admin.site.register(models.Estudiante)
admin.site.register(models.Profesor)

# Register your models here.
