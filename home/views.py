from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
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