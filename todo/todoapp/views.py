from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    tasks = task.objects.all()
    
    form = TaskForm()
    context = {'tasks': tasks,'form': form}     
    return render(request,'home.html',context)

def tasklist(request):
    return render(request,'task.html')

def timer(request):
    return render(request,'timer.html')
