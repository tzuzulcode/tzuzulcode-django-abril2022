from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CartItem, Cart
from products.models import Product
from django.utils.decorators import decorator_from_middleware
from users.middleware import AuthMiddleware
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from requests.auth import HTTPBasicAuth

paypal_url = "https://api-m.sandbox.paypal.com"

# Create your views here.
auth_middleware = decorator_from_middleware(AuthMiddleware)

print(auth_middleware)


@auth_middleware
def get_cart(request):
    if request.user.is_authenticated:
        products = request.user.cart.products.all()
        total = 0
        for cartItem in products:
            total += cartItem.product.price * cartItem.amount
        return render(request, "pages/cart.html", {
            "products": products,
            "total": total
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


@csrf_exempt
def change_amount(request):
    print(request.user)
    if request.method == "POST":
        data = json.loads(request.body)

        amount = data['amount']
        id_item = data['idItem']

        cart_item = CartItem.objects.get(id=id_item)

        cart_item.amount = amount
        cart_item.save()

        cart_items = cart_item.cart.products.all()

        total = 0
        for cartItem in cart_items:
            total += cartItem.product.price * cartItem.amount

        return JsonResponse({
            "total": total
        })

def delete_from_cart(request, id_cart_item):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(pk=id_cart_item)
        if cart_item.cart.user == request.user:
            cart_item.delete()

            return redirect("/cart")

    return redirect("/")


def get_access_token():
    return "A21AAJ6ODMptp-ReDHRpKUSHWo1378r_P_cvn2yAuZs1FOxTmtKiQLg6ZbKGa4o6v5oxzR3y2kD457_TxswnCGw7ZubmLF3-g"

def generate_client_token(request):
    access_token = get_access_token()

    client_token_url = paypal_url + "/v1/oauth2/token"
    response = requests.post(client_token_url, headers={
        "Authorization": "Bearer "+access_token,
        "Accept-Language": "en_US",
        "Content-Type": "application/json",
    })

    print(response)