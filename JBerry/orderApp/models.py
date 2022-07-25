from django.db import models
from cartapp.models import CartItem
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    oid=models.IntegerField(primary_key=True, auto_created=True)
    cid=models.ForeignKey(CartItem, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20, null=False)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    addr=models.TextField(max_length=100)
    town=models.CharField(max_length=20)
    zipcode=models.SmallIntegerField(null=False)
    ph=models.CharField(max_length=15)
    comment=models.TextField(max_length=200)
    choices=(
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled')
    )
    status=models.CharField(choices=choices, max_length=30)

    def __str__(self) -> str:
        return super().__str__()