from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# signup view

def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        try:
            user=User.objects.create_user(username=username,password=password,email=email)
            return redirect('signin')
        except Exception as e:
            error_message=str(e)  
    return render(request,'accounts/signup.html')

# signin view

def signin(req):
    if req.POST:
        username= req.POST.get('username')
        password= req.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            login(req,user)
            return redirect('home')
        else:
            messages.error(req,'Invalid username or password')

    return render(req,'accounts/signin.html')

# logout view

@login_required(login_url='signin')
def user_logout(req):
    logout(req)
    return redirect('signin')