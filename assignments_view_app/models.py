from django.db import models
# from django.contrib.auth.models import User
from classroom_app import settings

# Create your models here.
class Assignment(models.Model):
    poster= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    title=models.CharField(max_length=500, default="")
    text=models.TextField()
    question_content=models.FileField()
    is_done=models.BooleanField()
    # answer_content=models.FileField()
    # student_private_comment=models.CharField(max_length=1000, default="")