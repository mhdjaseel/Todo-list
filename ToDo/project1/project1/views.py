
from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth.decorators import login_required


#view for home
@login_required(login_url='signin')
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

@login_required(login_url='signin')

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
@login_required(login_url='signin')

def edit(request,id):
    task=Todo.objects.get(id=id)
    if request.method =='POST':
        task.item=request.POST.get('updateditem',task.item)
        task.save()
        return redirect('home')
    return render(request,'edit.html',{'task':task})


#view for change status to completed
@login_required(login_url='signin')

def completed(request,id):
    task=Todo.objects.get(id=id)
    task.status=True
    task.save()
    return redirect('home')


#view for completed task
@login_required(login_url='signin')

def completed_task(request):
    task=Todo.objects.all().filter(status=True)
    return render(request,'completed.html',{'task':task})

#view for profile
@login_required(login_url='signin')

def profile(request):
    user=request.user
    return render(request,'profile.html',{'user':user})