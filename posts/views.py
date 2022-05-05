from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'home.html')


def posts(request):
    posts = Post.objects.all()  # SELECT * FROM posts

    print(posts)
    # return HttpResponse("Publicaciones")

    return render(request, 'posts.html', {
        'posts': posts
    })


def post(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'post.html', {'post':post})
