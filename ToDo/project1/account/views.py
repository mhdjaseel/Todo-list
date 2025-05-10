from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



#signin view

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('home')
        else:
             messages.error(request,'invalid username or password')

    return render(request,'accounts/signin.html')



# signup view

def signup(request):
    form=AccountForm()
    if request.POST:
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(request,'accounts/singup.html',{'form':form})



#logout view

@login_required
def user_logout(request):
    logout(request)
    return redirect('signin')