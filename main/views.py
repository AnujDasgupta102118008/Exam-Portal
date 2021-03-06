from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('prof:index', prof_username=username)
        else:
            return redirect('main:index')

    return render(request, 'main/login.html')

def home(request, username):
    user = User.objects.get(username=username)
    return render(request, 'main/user_home.html',{
        'user': user
    })

def logoutUser(request):
    logout(request)
    return redirect('main:index')