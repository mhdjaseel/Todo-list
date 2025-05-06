
from django.shortcuts import render,redirect
from .models import Todo

#view for home
def home(request):
    context={}
    if request.method =='POST':    
        item=request.POST.get('todoInput')
        Todo.objects.create(item=item)
        return redirect('home')
    task = Todo.objects.all().order_by('-created_at')
    context={'task':task}
    return render(request,'layout.html',context)

#view for delete

def delete(request, id):
    item=Todo.objects.get(id=id)
    if request.method =='POST':    
        item.delete()
        return redirect('home')
    return render(request,'deletion.html',{'item':item})

#view for edit

def edit(request,id):
    task=Todo.objects.get(id=id)
    if request.method =='POST':
        task.item=request.POST.get('updateditem',task.item)
        task.save()
        return redirect('home')
    return render(request,'edit.html',{'task':task})

#view for completed

def completed(request):
    return render(request,'completed.html')