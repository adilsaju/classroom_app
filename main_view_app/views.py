from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

@login_required(login_url='/accounts/login')
def index(request):
    print("hello world!!!!!!")
    context={'key1':'val1'}
    return render(request,"main.html",context)

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request,'registration/register.html',context)
