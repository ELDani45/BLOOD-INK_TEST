from django import forms


class Login(forms.Form):
    user = forms.CharField(label="Ingresa tu usario", max_length=15)
    password = forms.CharField(label="Ingresa tu contarseña", max_length=15)
