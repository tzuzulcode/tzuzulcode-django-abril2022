from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'home.html')


def posts(request):
    posts = Post.objects.all()  # SELECT * FROM posts

    print(posts)
    # return HttpResponse("Publicaciones")

    return render(request, 'posts/posts.html', {
        'posts': posts
    })


def post(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'posts/post.html', {'post':post})


def create_post(request):
    if request.method == "POST":
        post = Post(
            title=request.POST['title'],
            description=request.POST['description'],
            img=request.POST['image'],
            content=request.POST['content']
        )

        post.save()

        return redirect("/posts")

    return render(request, 'posts/create.html')
