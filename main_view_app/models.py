from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Post(models.Model):
    #FIXME: not User, actually TeacherUser
    #manytoone
    poster= models.ForeignKey(User, on_delete=models.CASCADE, default="")
    post_time=models.DateTimeField(default=datetime.now)
    #or TextField?
    text = models.CharField(max_length=1000, default="")
    def __str__(self):
        return self.post_time

class StreamComment(models.Model):
    # poster= models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True, null=True)
    text=models.CharField(max_length=1000, default="")
    post_time=models.DateTimeField(default=datetime.now)
    corres_post=models.ForeignKey(Post, on_delete=models.CASCADE, default="")

class StudentUser(User):
    pass
class TeacherUser(User):
    pass

# #to remove
# class FileTest(models.Model):
#     file_given=models.BinaryField()

# class NewsItem(models.Model):
#     url = models.CharField(max_length=500, default="",unique=True)
#     title = models.CharField(max_length=500, default="")
#     hacker_news_url = models.CharField(max_length=500, default="")
#     posted_on = models.DateTimeField(default=datetime.now)
#     # posted_on = models.CharField(max_length=100,default="")
#     upvote_count = models.IntegerField(default=0)
#     comment_count = models.IntegerField(default=0)
#     # contents=models.TextField(default="")
#     users = models.ManyToManyField(User, verbose_name="Readers", related_name="reads")

#     def __str__(self):              # __unicode__ on Python 2
#         return self.url
