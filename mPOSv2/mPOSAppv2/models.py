from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class T_registration(models.Model):
    reg_id = models.IntegerField(default=1)
    fname = models.CharField(unique=False, max_length=50, null=False)
    lname = models.CharField(unique=False, max_length=50, null=False)
    email=models.EmailField(unique=True, max_length=50)
    phone=models.CharField(unique=True, max_length=150)
    address = models.CharField(unique=False, max_length=50, null=False)
    country = models.CharField(unique=False, max_length=50, null=False)
    username=models.CharField(unique=True, max_length=25, null=False, default='NA')
    password=models.CharField(max_length=16, null=False)

class T_messages(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name=models.CharField(unique=False, max_length=50)
    email=models.EmailField(unique=True, max_length=50)
    subject=models.CharField(unique=False, max_length=50)
    message=models.CharField(unique=False, max_length=500)

class T_category(models.Model):
    catid = models.IntegerField(primary_key=True, auto_created=True)
    catactive = models.CharField(max_length=50)
    catname = models.CharField(max_length=100)




def __str__(self) -> str:
    return f'{self.username} | {self.uid}'
