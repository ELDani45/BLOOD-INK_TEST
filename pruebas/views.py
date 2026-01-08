from django.shortcuts import render, redirect
from .models import Preguntas, Answer, Book, Author
from .forms import Createauthor
# from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def encuestas(request):
    questions = list(Preguntas.objects.all())
    choices = Answer.objects.all()
    return render(request, "encuestas.html", {
        "questions": questions,
        "choices": choices

    })


def autores(request):
    libros = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'autores.html', {
        'Books': libros, "Authors": authors
    })


def create_authors(request):
    if request.method == "GET":
        return render(request, "create_authors.html", {"form_authors": Createauthor})

    if request.method == "POST":
        form = Createauthor(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "EL usuario ha sido creado correctamente")
            return redirect("autores")

        else:
            form = Createauthor(data=request.POST)
            messages.error(request, "El usuario no es valido")
            return render(request, "create_authors.html", {"author_form": form})


def author_blog(request, id) -> object:
    object1 = Author.objects.get(id=id)
    return render(request, "author_blog.html", {
        'author_info': object1
    })
