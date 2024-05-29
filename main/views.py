from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Covid

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password'] == request.POST['confirmP']:
            try:
                #registrando un usuario
                user = User.objects.create_user(username=request.POST['usuario'],password=request.POST['password'])
                user.save()
                login(request,user)
                return redirect('inicio')
            except IntegrityError:
                return render(request,'signup.html',{
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request,'signup.html',{
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

def signin(request):

    if request.method =='GET':    
        return render(request,'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['usuario'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request,user)
            return redirect('inicio')

def inicio(request):
    datos = []
    #datos.append( Covid.objects.values_list("deaths",flat=True).filter(country_region="Albania"))
    #datos.append( Covid.objects.values_list("deaths",flat=True).filter(country_region="Kuwait"))
    datos.append( Covid.objects.values_list("deaths",flat=True).filter(country_region="Mexico").get() )
    datos.append( Covid.objects.values_list("deaths",flat=True).filter(country_region="Peru").get() )
    datos.append( Covid.objects.values_list("deaths",flat=True).filter(country_region="Chile").get() )
    datos.append( Covid.objects.values_list("deaths",flat=True).filter(country_region="Colombia").get() )
    print(datos)
    return render(request,'inicio.html',{'datos': datos})

def signout(request):
    logout(request)
    return redirect('signin')