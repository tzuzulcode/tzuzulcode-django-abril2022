from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, get_user_model
from json import loads
from django.db import IntegrityError
User = get_user_model()


@api_view(['POST'])
def login_view(request):
    data = loads(request.body)
    user = authenticate(request._request, email=data['email'], password=data['password'])

    if user is not None:
        if user.is_active:
            login(request._request,user)

        return Response({
            "success": True,
            "user": "Tzuzul"
        })

    return Response({
        "success": False,
        "message": "Incorrect credentials"
    })


@api_view(['POST'])
def signup_view(request):
    try:
        data = loads(request.body)
        user = User.objects.create_user(email=data['email'], password=data['password'], username=data['username'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()

        login(request._request, user)
        return Response({
            "success": True,
            "user": "Tzuzul"
        })
    except IntegrityError:
        return Response({
            "success": False,
            "message": "Verify your data"
        })