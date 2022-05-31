from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cart, name="cart"),
    path('add/<int:idProduct>', views.add_to_cart, name="add_to_cart")
]