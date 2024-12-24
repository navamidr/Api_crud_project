from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length=150)
    job = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Person(models.Model):
    role_choice=[
        ('MANAGER','manager'),
        ('EMPLOYEE','employee'),
    ]
    
    user_id = models.CharField(max_length=50,unique=True,editable=False,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    place = models.CharField(max_length=150)
    job = models.CharField(max_length=150)
    role = models.CharField(max_length=10,choices= role_choice,default='EMPLOYEE')


    def __str__(self):
        return self.name 
         

