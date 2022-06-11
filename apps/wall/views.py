from multiprocessing import context
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from ..logreg.models import User
from django.contrib import messages

# the index function is called when root is visited
def index(request):
    if 'logged_user' not in request.session:
        messages.success(request, "Not logged in!")
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['logged_user']),
        "messages": Message.objects.all().order_by("-created_at"),
    }
    return render(request, "wall/index.html", context)

def new_message(request):
    user = User.objects.get(id=request.session["logged_user"])
    if request.method == "POST":
        mes = Message.objects.create(message=request.POST['message'], user=user)
        return redirect('/wall')

def new_comment(request):
    print("in new comments, id for msg is: ", request.POST['msg_id'])
    user = User.objects.get(id=request.session["logged_user"])
    message = Message.objects.get(id=request.POST['msg_id'])
    if request.method == "POST":
        Comment.objects.create(comment=request.POST['comment'], user=user, message=message)
        return redirect('/wall')

def like_message(request, num):
    print("in likes")
    user = User.objects.get(id=request.session["logged_user"])
    msg = Message.objects.get(id=num)
    msg.likes_on_messages.add(user)
    msg.save()
    return redirect('/wall')

def like_comment(request, num):
    user = User.objects.get(id=request.session["logged_user"])
    cmnt = Comment.objects.get(id=num)
    cmnt.likes_on_comment.add(user)
    cmnt.save()
    return redirect('/wall')

def dislike(request, num):
    user = User.objects.get(id=request.session["logged_user"])
    msg = Message.objects.get(id=num)
    msg.likes_on_messages.remove(user)
    msg.save()
    return redirect('/wall')

def dislike_c(request, num):
    user = User.objects.get(id=request.session["logged_user"])
    cmnt = Comment.objects.get(id=num)
    cmnt.likes_on_comment.remove(user)
    cmnt.save()
    return redirect('/wall')

def destroy_message(request, num):
    msg = Message.objects.get(id=num)
    msg.delete()
    return redirect('/wall')

def destroy_comment(request, num):
    comment = Comment.objects.get(id=num)
    comment.delete()
    return redirect('/wall')

def logout(request):
    del request.session['logged_user']
    return redirect('/')
