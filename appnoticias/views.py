from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages
from .models import Noticia


# Create your views here.


def index(request):
    context={}
    return render(request, 'appnoticias/index.html')

def login_view(request):
    context={}
    return render(request, 'appnoticias/login.html')


def mas_noticias(request):
    context={}
    return render(request, 'appnoticias/mas_noticias.html')


def noticia(request):
    noticias= Noticia.objects.all()
    context={"noticias":noticias}
    return render(request, 'appnoticias/noticia.html', context)


def register(request):
    context={}
    return render(request, 'appnoticias/register.html')


def sobre_nosotros(request):
    context={}
    return render(request, 'appnoticias/sobre_nosotros.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('appnoticias:index')  # Corregir aquí
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')     
                
    else:
        form = LoginForm()

    return render(request, 'appnoticias/login.html', {'form': form})


