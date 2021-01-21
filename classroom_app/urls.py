"""classroom_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_view_app import views as main_views
from assignments_view_app import views as assignment_views
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_views.index),
    path('home/', main_views.index),
    path('classwork/', assignment_views.classwork_page),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', main_views.register, name='register'),
    path('about/', main_views.about),

    path('add/post', main_views.add_post),
    path('add/<int:post_id>/comment', main_views.add_comment),
    # path('hide/<int:news_item_pk>/', views.hide),
]
