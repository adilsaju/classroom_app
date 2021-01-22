from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login')
def classwork_page(request):
    print("hello assignments!!!!!!")
    context={'key1':'val1'}

    posts=Assignment.objects.all().order_by('-post_time')
    comments=PrivateAssignmentComment.objects.all().select_related('corres_post').order_by('-post_time')

    # print(comments)
    context={'all_posts':posts, 'all_post_comments': comments }
    return render(request,"index1.html",context)

@csrf_exempt
@login_required(login_url='/accounts/login')
def add_assignment(request):
    if request.method=="POST":
        post_content = request.POST['text']
        #to remove
        file1 = request.POST['file1'].encode()
        # obj2=FileTest(file_given=file1)
        # obj2.save()
        obj=Assignment(poster=request.user,post_time=datetime.now(),text=post_content,question_content=file1)
        obj.save()
        return HttpResponse("added assignment succ")
    else: 
        return render(request,'add-assignment.html')

@csrf_exempt
@login_required(login_url='/accounts/login')
def download_blob(request):
# def download_blob(request, id):

    contents = Assignment.objects.get(id=1).question_content

    response = HttpResponse(contents)
    response['Content-Disposition'] = 'attachment; filename=blob.bin'
    return response
