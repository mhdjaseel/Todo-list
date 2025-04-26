from django import views
from django.shortcuts import render,redirect
from .model import Todo

def home(request):
    if request.POST:
        item=request.POST.get('todoInput')
        Todo.objects.create(item=item)
        return redirect('home')
    return render(request,'home.html')