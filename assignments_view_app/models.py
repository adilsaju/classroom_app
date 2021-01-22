from django.db import models
# from django.contrib.auth.models import User
from classroom_app import settings
from datetime import datetime
# Create your models here.
class Assignment(models.Model):
    poster= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    # text=models.TextField()
    text = models.CharField(max_length=1000, default="")
    # title=models.CharField(max_length=500, default="")
    #TODO: multiple media files how?
    question_content=models.BinaryField()
    # is_done=models.BooleanField()
    post_time=models.DateTimeField(default=datetime.now)

    # answer_content=models.FileField()
    # student_private_comment=models.CharField(max_length=1000, default="")
class PrivateAssignmentComment(models.Model):
    poster= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="", blank=True, null=True)
    text=models.CharField(max_length=1000, default="")
    post_time=models.DateTimeField(default=datetime.now)
    corres_post=models.ForeignKey(Assignment, on_delete=models.CASCADE, default="")

class PublicAssignmentComment(models.Model):
    poster= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="", blank=True, null=True)
    post_time=models.DateTimeField(default=datetime.now)
    text=models.CharField(max_length=1000, default="")
    corres_post=models.ForeignKey(Assignment, on_delete=models.CASCADE, default="")

#onetime post only. to repost, have to withdraw current or edit current
class PrivateAssignmentSubmission(models.Model):
    poster= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="", blank=True, null=True)
    post_time=models.DateTimeField(default=datetime.now)
    corres_post=models.ForeignKey(Assignment, on_delete=models.CASCADE, default="")
    is_edited=models.BooleanField()
    is_late=models.BooleanField()
    is_graded=models.BooleanField()
    grade=models.IntegerField(default=0)

#TODO: add general material & public comment- model as well