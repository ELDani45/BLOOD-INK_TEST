import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# Cada campo esta representando por una instancia "Field" :
# - Por ejemplo, "CharField" para campos de caracteres y "DateTimeField" para variables de tiempo y fecha. Esto le dice a Django qué tipo de datos cada campo contiene.


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        # Esto hace que envie los datos de forma de strings cuando pidamos los datos en el shell de python por ejemplo
        return str(self.question_text)

    def was_published_recently(self):
        return self.pub_date >= timezone.now()

    datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)


class Preguntas(models.Model):
    text = models.TextField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    objects = CustomManager()


class Answer(models.Model):
    QUESTION_TYPES = (
        ("DonCat", "a"),
        ("Wiskas", "b"),
        ("Felix", "c")
    )

    question = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    answer = models.CharField(
        max_length=10, choices=QUESTION_TYPES, default="single")

    def __str__(self):
        return str(self.answer)

    objects = CustomManager()
