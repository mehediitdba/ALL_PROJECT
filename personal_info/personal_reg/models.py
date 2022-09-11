from turtle import title
from django.db import models

# Create your models here.

class Position(models.Model):
    title=models.CharField(max_length=50)

class Personal(models.Model):
    fullname=models.CharField(max_length=100),
    per_code=models.CharField(max_length=15),
    mobile=models.CharField(max_length=15),
    position=models.ForeignKey(Position,on_delete=models.CASCADE)

