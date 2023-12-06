from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    rank = models.IntegerField()
    telefon = models.CharField(max_length=100, default='-')
    balance = models.IntegerField()
    
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    
class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')