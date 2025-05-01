
from django.shortcuts import render,redirect
from .models import Todo

def home(request):
    context={}
    if request.method =='POST':    
        item=request.POST.get('todoInput')
        Todo.objects.create(item=item)
        task = Todo.objects.all().order_by('-created_at')
        context={'task':task}
    return render(request,'home.html',context)
