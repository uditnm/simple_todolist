from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def index(request):
    todolist = Todo.objects.filter(user=request.user)
    if request.method == "POST":
        Todo1 = Todo(
            task=request.POST['task'],user = request.user)
        Todo1.save()
        return redirect("index")
    return render(request, "index.html", {"todolist":todolist})

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("index")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            messages.info(request, "email already used")
            return redirect("register")
        elif User.objects.filter(username=username).exists():
            messages.info(request,"name already in use")
            return redirect("register")
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save;
            return redirect("login")
    else:
        return render(request, "register.html")

def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("index")
        else:
            messages.info(request,"credentials invalid")
            return redirect("login")

    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")


