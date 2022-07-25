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


    def __str__(self) -> str:
        return f'{self.username} | {self.uid}'
