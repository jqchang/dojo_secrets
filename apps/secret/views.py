from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import User, Message
# Create your views here.
def index(request):
    if "id" in request.session:
        user = User.objects.get(id=request.session["id"])
        secrets = Message.objects.annotate(numlikes=Count('likes')).order_by('created_at')
        return render(request, 'secret/index.html', {"user":user, "secrets":secrets})
    else:
        messages.info(request, "Please log in below.")
        return redirect('login:login_index')

def process(request):
    if request.method != 'POST':
        return redirect('/secret')
    messages.info(request, "Work in progress!")
    message = Message.objects.validate(request.POST, request.session["id"])
    return redirect('/secret')

def popular(request):
    user = User.objects.get(id=request.session["id"])
    messages = Message.objects.annotate(numlikes=Count('likes')).order_by('-numlikes')
    liked = Message.objects.filter(likes=user)
    return render(request, 'secret/popular.html', {"secrets":messages, "user":user})

def delete(request, id):
    try:
        target = Message.objects.get(id=id)
    except Message.DoesNotExist:
        messages.info(request, "Message not found!")
        return redirect('secret:secret_index')
    target.delete()
    return redirect('secret:secret_index')

def like(request, message_id):
    like_valid = Message.objects.createLike(request.session["id"], message_id)
    print "like_valid", like_valid
    return redirect('secret:secret_index')
