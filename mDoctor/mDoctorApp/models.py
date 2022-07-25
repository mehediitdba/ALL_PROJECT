from django.db import models

# Create your models here.

# Create your models here.

class T_Appiontment(models.Model):
    appid=models.BigIntegerField(null=True)
    app_name=models.CharField(max_length=60)
    app_email=models.EmailField(max_length=50)
    app_phone=models.CharField(max_length=20)
    app_date=models.DateField()
    app_dept=models.CharField(max_length=20)
    app_doc=models.CharField(max_length=20)
    app_comments=models.CharField(max_length=200)

def __str__(self) -> str:
    return f'{self.pid} | {self.title}'