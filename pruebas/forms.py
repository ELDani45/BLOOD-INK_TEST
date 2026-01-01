# Esto importa todos los modelos de formularios que tiene Django
from django import forms
from pruebas.models import Author


# [ ModelForm ] = Modelo predeterminado de Django
class Createauthor(forms.ModelForm):

    class Meta:
        model = Author  # Trae el modelo en especifico donde se relaciona con el formualario
        fields = '__all__'
        # Esto le dice que campos va a traer el formulario del modelo, si los campos son especificos se hace de esta manera:
        # fields = ('name', 'last_name', 'age')
