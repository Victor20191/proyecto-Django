"""
URL configuration for djangoCrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from tareas import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/tareasFinalizadas/', views.tareasFinalizadas, name='tareasFinalizadas'),
    path('tareas/creacion/', views.creacionTareas, name='creacionTareas'),
    path('tareas/<int:tarea_id>', views.detalleTareas, name='detalleTareas'),
    path('tareas/<int:tarea_id>/completada', views.tareasCompletadas, name='tareasCompletadas'),
    path('tareas/<int:tarea_id>/borrarTareas', views.borrarTareas, name='borrarTareas'),
    path('cerrarSesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
]
