from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.IntegerField(primary_key=True, auto_created=True)
    username=models.CharField(unique=True, max_length=25, null=False, default='NA')
    email=models.EmailField(unique=True, max_length=50)
    password=models.CharField(max_length=16, null=False)

    def __str__(self) -> str:
        return f'{self.username} | {self.uid}'

class Email(models.Model):
    emailid =models.IntegerField(primary_key=True, auto_created=True)
    username=models.CharField(unique=True, max_length=25, null=False, default='NA')
    email=models.EmailField(unique=True, max_length=50)
    subject=models.CharField( max_length=50)
    messagebody=models.CharField( max_length=500)
