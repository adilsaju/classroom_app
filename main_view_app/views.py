from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login')
def index(request):
    print("hello world!!!!!!")
    context={'key1':'val1'}
    return render(request,"main.html",context)