from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def classwork_page(request):
    print("hello assignments!!!!!!")
    context={'key1':'val1'}
    return render(request,"index1.html",context)