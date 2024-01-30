from django.shortcuts import render

# Create your views here.


def index(request):
    context={}
    return render(request, 'appnoticias/index.html', context)

def login(request):
    context={}
    return render(request, 'appnoticias/login.html')


def mas_noticias(request):
    context={}
    return render(request, 'appnoticias/mas_noticias.html')


def noticia(request):
    context={}
    return render(request, 'appnoticias/noticia.html')


def register(request):
    context={}
    return render(request, 'appnoticias/register.html')


def sobre_nosotros(request):
    context={}
    return render(request, 'appnoticias/sobre_nosotros.html')



