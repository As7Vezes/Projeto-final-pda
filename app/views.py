from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Chamando arquivo html 'sobre'
def sobre(request):
    return render(request, 'sobre.html')

# Chamando arquivo html 'contato'
def contato(request):
    return render(request, 'contato.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user_exists = User.objects.filter(username=usuario).exists()
        email_exists = User.objects.filter(email=email).exists()

        if user_exists:
            mensagem_erro = 'Usuário já existe.'
            return render(request, 'cadastro.html', {'mensagem_erro': mensagem_erro})
        elif email_exists:
            mensagem_erro = 'Email já existe.'
            return render(request, 'cadastro.html', {'mensagem_erro': mensagem_erro})
        else:
            user = User.objects.create_user(username=usuario, email=email, password=senha)
            user.save()
            return redirect('login')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)

        if user:
            login_django(request, user)
            return redirect('home')
        else:
            mensagem_erro = 'Email ou senha inválidos'
            return render(request, 'login.html', {'mensagem_erro': mensagem_erro})
        
def user(request):
    return render (request, 'usuario.html')

