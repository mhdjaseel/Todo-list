from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# signup view

def signup(request):
    form=AccountForm()
    if request.POST:
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(request,'accounts/signup.html',{'form':form})

# signin view

def signin(req):
    if req.POST:
        username= req.POST.get('username')
        password= req.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            return redirect('home')
        else:
            messages.error(req,'Invalid username or password')

    return render(req,'accounts/signin.html')

# logout view


def user_logout(req):
    logout(req)
    return redirect('signin')