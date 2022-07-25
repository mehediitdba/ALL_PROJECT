from django.db import models
from django.contrib.auth.models import User
from productApp.models import Product

# Create your models here.
class CartItem(models.Model):
    cid=models.IntegerField(primary_key=True, auto_created=True)
    uid=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pid=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty=models.SmallIntegerField(default=0)
    price=models.FloatField(default=0.0)
    ordered=models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.cid)