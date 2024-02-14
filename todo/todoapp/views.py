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

def edit(request, pk):
    task = task.objects.get(id=pk)
    return render(request,'edittask.html') 

def timer(request):
    return render(request,'timer.html')
