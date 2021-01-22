from .models import User
from django.contrib.auth.forms import UserCreationForm

class ClassAddForm(UserCreationForm):
   # here is the important part.. add a class Meta-
   class Meta:
      model = User
      fields = ('username', 'password1', 'password2', 'class_member_type')