from django import forms

from . import models

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"
        
        
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = "__all__"

class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = ['nombre', 'comision', 'profesor']        