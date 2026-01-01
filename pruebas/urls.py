from django.urls import path
from . import views

urlpatterns = [
    path("", views.encuestas, name="encuesta"),
    path('autores/', views.autores, name='autores')
]
