from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
# Create your views here.


# signup view

def signup(request):
    form=AccountForm()
    if request.POST:
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'accounts/singup.html',{'form':form})