from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'index.html')

# def login(request):
#     return render(request,"login.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home:index")

    return render(request,'login.html')

def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("home:index")
        return redirect("home:login")
    return render(request,"login.html")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home:index")