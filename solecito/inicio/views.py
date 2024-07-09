from django.shortcuts import render
from .models import Tarea
from .models import Evento

def home(request):
    return render(request, "inicio/home.html")

def about(request):
    return render(request, "inicio/about.html")

def calendario(request):
    eventos=Evento.objects.all()
    return render(request, "inicio/calendario.html",{'eventos':eventos})

def tareas(request):
    tareas=Tarea.objects.all()
    return render(request, "inicio/tareas.html",{'tareas':tareas})

def contacto(request):
    return render(request, "inicio/contacto.html")

