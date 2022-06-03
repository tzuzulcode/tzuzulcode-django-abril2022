from django.shortcuts import render, redirect
from .models import CartItem, Cart
from products.models import Product


# Create your views here.
def get_cart(request):
    if request.user.is_authenticated:
        products = request.user.cart.products.all()

        return render(request, "pages/cart.html", {
            "products": products
        })

    return redirect("/")


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


def delete_from_cart(request, id_cart_item):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(pk=id_cart_item)
        if cart_item.cart.user == request.user:
            cart_item.delete()

            return redirect("/cart")

    return redirect("/")
