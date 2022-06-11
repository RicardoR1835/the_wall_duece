from multiprocessing import context
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# the index function is called when root is visited
def index(request):
    return render(request, "logreg/index.html")

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if request.method == "POST":
        user = User.objects.create(first_name=request.POST["fn"], last_name=request.POST["ln"], email=request.POST["email"], password=request.POST['password'])
        request.session["logged_user"] = user.id
        return redirect('/wall')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['logged_user'] = user.id
    messages.success(request, "User was successfully logged in")
    return redirect('/wall')

