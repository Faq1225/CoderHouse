from django import forms

class estudianteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class profesorForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    materiaQueDa = forms.CharField(max_length=40)

class materiaForm(forms.Form):
    nombre = forms.CharField(max_length=40)