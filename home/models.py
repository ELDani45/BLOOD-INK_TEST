from django.db import models


# Create your models here.
class Acount(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return "-" + " " + self.user + "--" + self.password
