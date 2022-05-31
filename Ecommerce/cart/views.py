from django.shortcuts import render,redirect
from .models import CartItem,Cart
from products.models import Product

# Create your views here.
def get_cart(request):
    return render(request,"pages/cart.html")


def add_to_cart(request, idProduct):
    if request.user.is_authenticated:
        cartItem = CartItem()
        cartItem.product = Product.objects.get(pk=idProduct)
        cartItem.amount = 1
        if request.user.cart:
            cartItem.cart = request.user.cart
        else:
            cart = Cart()
            cart.user = request.user
            cart.save()
            cartItem.cart = cart

        cartItem.save()

    return redirect("/")
