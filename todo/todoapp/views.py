from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import task
def home(request):
    tasks = task.objects.all()
    context = {'tasks': tasks}     
    return render(request,'home.html',context)

def tasklist(request):
    return render(request,'task.html')

def timer(request):
    return render(request,'timer.html')
