from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate  #login crea la sesion (cookie)
from django.db import IntegrityError
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def welcome(request):
    return render(request,'welcome.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)   #Crea la sesión en el navegador (cookie)
                return render(request,'welcome.html')
            except IntegrityError:
                return render(request, 'users/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'users/signup.html', {
                    'form': UserCreationForm,
                    'error': 'Contraseñas no coinciden'
                })