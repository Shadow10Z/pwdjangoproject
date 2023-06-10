from django.shortcuts import render
import datetime

# Create your views here.

def index_page_view(request):	
    return render(request, 'portfolio/index.html')

def index2_page_view(request):
	return render(request, 'portfolio/index2.html')

def index3_page_view(request):
	return render(request, 'portfolio/index3.html')