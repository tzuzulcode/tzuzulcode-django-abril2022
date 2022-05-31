from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")


# Create your models here.
class CartItem(models.Model):
    amount = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


