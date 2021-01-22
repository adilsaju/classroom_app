from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from _datetime import datetime
import parsedatetime
# from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from .models import *
import copy
from .forms import *
from django.contrib.auth.decorators import user_passes_test


#about***
@login_required(login_url='/accounts/login')
def about(request):
    return render(request,'about.html') 

#registration stuff**
def register(request):
    if request.method=="POST":
        # class_member_type=request.POST['class_member_type']
        form=ClassAddForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
    else:
        # form=UserCreationForm()
        form= ClassAddForm()
    context={'form':form}
    return render(request,'registration/register.html',context)

#main page logic***
@login_required(login_url='/accounts/login')
def index(request):
    print("hello world!!!!!!")
    context={'key1':'val1'}

    posts=Post.objects.all().order_by('-post_time')
    comments=StreamComment.objects.all().select_related('corres_post').order_by('-post_time')
    # print(comments)
    context={'all_posts':posts, 'all_post_comments': comments }
    return render(request,"index.html",context)

@login_required(login_url='/accounts/login')
def search(request):
    print("hello world!!!!!!")
    context={'key1':'val1'}

    # posts=Post.objects.all().order_by('-post_time')
    # comments=StreamComment.objects.all().select_related('corres_post').order_by('-post_time')
    # print(comments)
    # context={'all_posts':posts, 'all_post_comments': comments }
    return HttpResponse("hello world search!!!!")

def is_teacher(user):
    try:
        return user.is_authenticated and user.class_member_type == "teacher"
    except User.DoesNotExist:
        return False


@user_passes_test(is_teacher)
@csrf_exempt
@login_required(login_url='/accounts/login')
def add_post(request):
    if request.method=="POST":
        post_content = request.POST['post']
        #to remove
        # file1 = request.POST['file1'].encode()
        # obj2=FileTest(file_given=file1)
        # obj2.save()

        obj=Post(poster=request.user,post_time=datetime.now(),text=post_content)
        obj.save()
        return HttpResponse("added post")
    else: 
        return render(request,'add-news-item.html')
@csrf_exempt
@login_required(login_url='/accounts/login')
def add_comment(request, post_id):
    if request.method=="POST":
        comment1 = request.POST['comment']
        print("###############poster")
        print(request.user)
        print(comment1)
        print(post_id)

        obj=StreamComment(poster=request.user,text=comment1,post_time=datetime.now(),corres_post_id=post_id)
        obj.save()
        return HttpResponse("added comment")
    else: 
        return render(request,'index.html')