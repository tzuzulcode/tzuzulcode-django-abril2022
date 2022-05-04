from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def posts(request):
    posts = Post.objects.all() # SELECT * FROM posts

    print(posts)
    return HttpResponse("Publicaciones")