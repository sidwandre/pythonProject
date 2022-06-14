from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.auth import *


# Create your views here.

def user_login(request):
    if request.method == "GET":
        return render(request, 'systemUser/login.html')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pwd']
        username = User.objects.get(email=email)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            # print(email,password)
            return HttpResponse('FAIL')


def signUp(request):
    if request.method == "GET":
        return render(request, 'systemUser/signUp.html')
    if request.method == "POST":
        User.username = request.POST['username']
        User.password = request.POST['pwd']
        User.email = request.POST['email']
        u = User.objects.create_user(User.username, User.email, User.password)
        u.save()
    return render(request, 'systemUser/signUp.html')

