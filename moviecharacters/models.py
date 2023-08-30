# import models
from django.db import models

class Character(models.Model):
    movie = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    first_appearance = models.CharField(max_length=255)

    def __str__(self):
        return self.name