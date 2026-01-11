from django.urls import path
from . import views

app_name = "pruebas"

urlpatterns = [
    path("", views.encuestas, name="encuesta"),
    path('autores/', views.autores, name='autores'),
    path("crate_author/", views.create_authors, name="make_authors"),
    path("author_blog/<int:id>/", views.author_blog, name='blog'),
    path("update/<int:id>/", views.update, name='update')
]
