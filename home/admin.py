from django.contrib import admin
from .models import Acount
from pruebas.models import Answer, Preguntas

# Register your models here.
admin.site.register(Acount)
admin.site.register(Preguntas)
admin.site.register(Answer)
