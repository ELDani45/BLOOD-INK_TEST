from django.db import models

# Create your models here.

# Cada campo esta representando por una instancia "Field" :
# - Por ejemplo, "CharField" para campos de caracteres y "DateTimeField" para variables de tiempo y fecha. Esto le dice a Django qué tipo de datos cada campo contiene.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        # Esto hace que envie los datos de forma de strings cuando pidamos los datos en el shell de python por ejemplo
        return str(self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
