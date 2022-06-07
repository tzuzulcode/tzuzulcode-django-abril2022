from django.shortcuts import render, redirect
from .models import CartItem, Cart
from products.models import Product
from django.utils.decorators import decorator_from_middleware
from users.middleware import AuthMiddleware

# Create your views here.
auth_middleware = decorator_from_middleware(AuthMiddleware)

print(auth_middleware)


@auth_middleware
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
        cartItem.cart = request.user.cart
        cartItem.save()

    return redirect("/")


def delete_from_cart(request, id_cart_item):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(pk=id_cart_item)
        if cart_item.cart.user == request.user:
            cart_item.delete()

            return redirect("/cart")

    return redirect("/")
