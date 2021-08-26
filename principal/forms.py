from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido','correo') # o si quieres todos '__all__'
