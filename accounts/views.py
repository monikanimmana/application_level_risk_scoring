from django.shortcuts import render
from django.contrib.auth import authenticate , login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
 
# Create your views here.
@api_view(['POST'])
def Register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if UserProfile.objects.filter(username=username).exists():
        return Response({'error':'username already exists'},status=400)
    
    user = UserProfile.objects.create_user(
        username = username,
        password = password,
        email = email,
    )

    return Response({'message': 'User is successfully created'})


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username = username,password=password)

    if user is None:
        return Response({'error':'User ceredials are invalid'}, status=401)
    
    if user.status == "blocked":
        return Response({'error':'Account is Blocked'}, status=403)
    
    user.last_ip = request.META.get('REMOTE ACCESS')
    user.last_device = request.META.get('HTTP_USER_AGENT')
    user.save()

    login(request,user)

    return Response({'message':'Login Successful'},status=200)

    
    