from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse
from .models import *
from.forms import *
from django.contrib.auth import logout as auth_logout


def home(request):
    # Filter tasks by the logged-in user
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = []  # or redirect to login if needed

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the current user to the task
            task.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todoapp/home.html', context)


def update_task(request, pk):
    tasks= Task.objects.get(id=pk)
    form=TaskForm(instance=tasks)
    if request.method == 'POST':
        form=TaskForm(request.POST, instance = tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'todoapp/update_task.html', context)




def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')  # Ensure you have a URL pattern for 'home' 

    return redirect('home')




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm() 
    return render(request, 'todoapp/signup.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'todoapp/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'todoapp/login.html')


def user_logout(request):  
    auth_logout(request)  
    return redirect('login') 




            
        