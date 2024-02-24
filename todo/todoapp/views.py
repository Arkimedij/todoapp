from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def tasklist(request):
    tasks = task.objects.all()
    
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('/')
    context = {'tasks': tasks,'form': form}  
    return render(request,'task.html',context)

def edit_task(request, pk):
    task_instance  = task.objects.get(id=pk)
    form = TaskForm(instance=task_instance)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task_instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request,'edittask.html',context) 

def Delete(request,pk):
    item  = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'delete.html',context)

def timer(request):
    return render(request,'timer.html')
