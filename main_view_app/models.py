from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Post(models.Model):
    pass

class StudentUser(User):
    pass
class TeacherUser(User):
    pass

class Assignment(models.Model):
    pass