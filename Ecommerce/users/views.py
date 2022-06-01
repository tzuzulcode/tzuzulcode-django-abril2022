from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

# Create your views here.
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect("/")
            else:
                return render(request, "pages/login.html", {
                    "error": "Inactive account"
                })
        return render(request, "pages/login.html", {
            "error": "Invalid credentials"
        })

    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "pages/login.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("/")


def signup_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']

        if password_confirmation!=password:
            return render(request, "pages/signup.html", {
                "error": "Password and password confirmation does not match"
            })

        try:
            new_user = User.objects.create_user(username,email,password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            login(request, new_user)
            return redirect("/")

        except IntegrityError:
            return render(request, "pages/signup.html", {
                "error": "Email or username already registered"
            })

    return render(request, "pages/signup.html")
