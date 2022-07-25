from cmath import pi
from email.mime import image
from turtle import title
from django.db import models

# Create your models here.

class Product(models.Model):
    pid=models.BigIntegerField(auto_created=True, primary_key=True)
    title=models.CharField(max_length=60)
    description=models.TextField(max_length=1000)
    price=models.FloatField()
    weight=models.FloatField()
    category=models.CharField(max_length=20)
    delivery=models.SmallIntegerField(default=7)
    stock=models.BooleanField(default=True)
    image=models.ImageField(upload_to='upload')

def __str__(self) -> str:
    return f'{self.pid} | {self.title}'