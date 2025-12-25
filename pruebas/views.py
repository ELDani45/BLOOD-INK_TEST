from django.shortcuts import render
from .models import Preguntas, Answer
# Create your views here.


def encuestas(request):
    questions = list(Preguntas.objects.all())
    choices = Answer.objects.all()
    return render(request, "encuestas.html", {
        "questions": questions,
        "choices": choices

    })
