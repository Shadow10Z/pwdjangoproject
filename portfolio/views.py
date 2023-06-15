from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime

# Create your views here.

def index_page_view(request):	
    return render(request, 'portfolio/index.html')

def index2_page_view(request):
	return render(request, 'portfolio/index2.html')

def index3_page_view(request):
	return render(request, 'portfolio/index3.html')

def home_page_view(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'portfolio/home.html', context)

def new_post_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:home')
    context = {'form': form}
    return render(request, 'portfolio/new.html', context)

def edit_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form, 'portfolio_id': post_id}
    return render(request, 'portfolio/edit.html', context)


def delete_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:home'))

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return redirect('portfolio:home')