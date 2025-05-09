
from django.shortcuts import render,redirect
from .models import Todo

#view for home
def home(request):
    context={}
    if request.method =='POST':    
        item=request.POST.get('todoInput')
        Todo.objects.create(item=item)
        return redirect('home')
    task = Todo.objects.all().filter(status=False)      #filter to get incomplete task
    context={'task':task}
    return render(request,'layout.html',context)


#view for delete

def delete(request, id):
    item=Todo.objects.get(id=id)
    next_page=request.GET.get("next","home")     # identify request frm which template
    if request.method =='POST':    
        item.delete()
        if next_page=="completed":
            remaining_completed = Todo.objects.filter(status=True).exists()    # check data is available in completed page or not
            if remaining_completed:
                return redirect("completed_task")
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


#view for change status to completed

def completed(request,id):
    task=Todo.objects.get(id=id)
    task.status=True
    task.save()
    return redirect('home')


#view for completed task

def completed_task(request):
    task=Todo.objects.all().filter(status=True)
    return render(request,'completed.html',{'task':task})