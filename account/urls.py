from django.urls import path

from . import views
app_name = "auth"
urlpatterns = [
    path("login/", views.user_login, name="login")
]
