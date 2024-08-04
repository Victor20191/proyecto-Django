from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .formularios import FormularioTareas
from .models import Tarea
from django.utils import timezone
def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                })
        else:
            return render(request, 'registro.html', {
                'form': UserCreationForm,
                'error': "Las contraseñas no coinciden"
            })

def tareas(request):
    tareas=Tarea.objects.filter(usuario=request.user,finalizado__isnull=True)
    return render(request, 'tareas.html',{'tareas':tareas})


def tareasFinalizadas(request):
    tareas=Tarea.objects.filter(usuario=request.user,finalizado__isnull=False).order_by('-finalizado')
    return render(request, 'tareas.html',{'tareas':tareas})

def creacionTareas(request):
    if request.method=='GET':
        return render(request,'creacion_tareas.html',{
        'form': FormularioTareas  
    })
    else: 
        try:
            formulario=FormularioTareas(request.POST)
            nuevaTarea=formulario.save(commit=False)
            nuevaTarea.usuario=request.user
            nuevaTarea.save()
            return redirect('tareas')
        except ValueError:
            return render(request,'creacion_tareas.html',{
            'form': FormularioTareas,
            'error': 'Por favor, ingresa datos reales'
    })

def detalleTareas(request, tarea_id):
    if request.method=='GET':  
        tarea = get_object_or_404(Tarea, pk=tarea_id,usuario=request.user)
        formulario = FormularioTareas(instance=tarea)
        return render(request, 'tareas_detalles.html', {'tarea': tarea, 'formulario': formulario})
    else:
        try:
            tarea=get_object_or_404(Tarea,pk=tarea_id,usuario=request.user)
            formulario=FormularioTareas(request.POST,instance=tarea)
            formulario.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tareas_detalles.html', 
            {'tarea': tarea, 'formulario': formulario,
            'error':'Erorr al actualizar tarea'})
        

def tareasCompletadas(request,tarea_id):
    tarea=get_object_or_404(Tarea,pk=tarea_id,usuario=request.user)
    if request.method=='POST':
        tarea.finalizado=timezone.now()
        tarea.save()
        return redirect('tareas')


def borrarTareas(request,tarea_id):
    tarea=get_object_or_404(Tarea,pk=tarea_id,usuario=request.user)
    if request.method=='POST':
        tarea.delete()
        return redirect('tareas')



def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

def iniciarSesion(request):
    if request.method == 'GET':        
        return render(request, 'iniciarSesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html', {
                'form': AuthenticationForm,
                'error': 'user y contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('tareas')
