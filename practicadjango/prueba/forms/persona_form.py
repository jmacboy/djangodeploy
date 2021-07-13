from django import forms

from prueba.models import Persona


class PersonaForm(forms.ModelForm):
    # nombres = forms.CharField(label='Nombres', max_length=100)
    # apellidos = forms.CharField(label='Apellidos', max_length=100)
    # ciudad = forms.CharField(label='Ciudad', max_length=100)
    # edad = forms.IntegerField(label='Edad')
    # fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput())
    # genero = forms.IntegerField(label='Género', widget=forms.Select(choices=Persona.GENERO_CHOICES))
    # email = forms.EmailField(label='Email', max_length=200)
    # direccion = forms.CharField(label="Dirección", max_length=500)

    class Meta:
        model = Persona
        fields = '__all__'
