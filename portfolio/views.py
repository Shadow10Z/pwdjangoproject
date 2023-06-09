from django.shortcuts import render
import datetime

# Create your views here.

def layout_page_view(request):
	
    currentTime = datetime.datetime.now()

    context = {'hora': currentTime.hour}

    return render(request, 'portfolio/layout.html', context)


def apresentacao_page_view(request):
	return render(request, 'portfolio/apresentacao.html')

def competencias_page_view(request):
	return render(request, 'portfolio/competencias.html')

def formacao_page_view(request):
	return render(request, 'portfolio/formacao.html')

def projetos_page_view(request):
	return render(request, 'portfolio/projetos.html')