from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length=150)
    job = models.CharField(max_length=150)

    def __str__(self):
        return self.name