from django.db import models

# Create your models here.
class Personal(models.Model):
    fullname=models.CharField(max_length=100)
    per_code=models.CharField(max_length=3)
    mobile=models.CharField(max_length=15)