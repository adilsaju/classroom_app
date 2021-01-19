from django.shortcuts import render

# Create your views here.
# @login_required(login_url='/accounts/login')
def classwork_page(request):
    print("hello assignments!!!!!!")
    context={'key1':'val1'}
    return render(request,"index.html",context)