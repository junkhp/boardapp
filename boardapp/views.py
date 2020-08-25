from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'boardapp/signup.html', {'error':'このユーザー名は既に登録されています．'})
        except:   
            user = User.objects.create_user(username2, '', password2)
            return redirect('login')
    return render(request, 'boardapp/signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'boardapp/login.html')

@login_required
def listfunc(request):
    context = {
        'object_list': BoardModel.objects.all(),
    }
    return render(request, 'boardapp/list.html', context)
    
def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    context = {
        'object': object,
    }
    return render(request, 'boardapp/detail.html', context)

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect('list')

def readfunc(request, pk):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    post = BoardModel.objects.get(pk=pk)
    if not username in post.readtext.split(','):
        post.read += 1
        post.readtext = post.readtext + username + ','
        post.save()
    return redirect('list')

class BoardCreateView(CreateView):
    template_name = 'boardapp/create.html'
    model = BoardModel
    fields = (
        'title',
        'content',
        'author',
        'images',
    )
    success_url = reverse_lazy('list')