from django.urls import path
from . import views

urlpatterns = [
    path("", views.encuestas, name="encuesta"),
    path('autores/', views.autores, name='autores'),
    path("crate_author/", views.create_authors, name="make_authors")
]
