"""portfolab5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.shortcuts import render
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('index', views.index_page_view, name='index'),
    path('index2', views.index2_page_view, name='index2'),
    path('index3', views.index3_page_view, name='index3'),
    path('home', views.home_page_view, name='home'),
    path('new/', views.new_post_view, name='new'),
    path('edit/<int:post_id>', views.edit_post_view, name='edit'),
    path('delete/<int:post_id>', views.delete_post_view, name='delete'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
