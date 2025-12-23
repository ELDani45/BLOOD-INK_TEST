from django.shortcuts import render
from .models import Question, Choice
# Create your views here.


def encuestas(request):
    question = Question.objects.all()
    choice = Choice.objects.all()
    return render(request, "encuestas.html", {
        "question": question,
        "choice": choice

    })
