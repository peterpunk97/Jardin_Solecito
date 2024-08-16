from django.shortcuts import render
from .models import Tarea
from .models import Evento
from .forms import ComentarioForm
from .models import Comentario
from django.http import HttpResponse
import os

#FUNCIONES PARA RENDERIZAR LOS TEMPLATES
def home(request):
    return render(request, "inicio/home.html")

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

def dudas(request):
    dudas=Comentario.objects.all()
    return render(request, "inicio/dudaslist.html",{'dudas':dudas})

def contacto(request):
    return render(request,"inicio/contacto.html")
#-----------------------------------------------------------------------------



#FUNCIÓN PARA PROCESAR LA INFORMACIÓN DEL FORMULARIO
def Registrar(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio/contacto.html')
        form = ComentarioForm()
        return render(request, 'inicio/contacto.html', {'form':form})
#-----------------------------------------------------------------------------


#FUNCIONES PARA RENDERIZAR LAS CONSULTAS DEL  FILTRADO DE TAREAS POR GRUPO
def consultarGrupo(request):
    tareas = Tarea.objects.filter(grupo__nombreGrupo="1A")
    return render(request, "inicio/consultasGrupo.html", {'tareas': tareas})


def consultarGrupo2(request):
    tareas = Tarea.objects.filter(grupo__nombreGrupo="1B")
    return render(request, "inicio/consultasGrupo2.html", {'tareas': tareas})


def consultarGrupo3(request):
    tareas = Tarea.objects.filter(grupo__nombreGrupo="2A")
    return render(request, "inicio/consultasGrupo3.html", {'tareas': tareas})


def consultarGrupo4(request):
    tareas = Tarea.objects.filter(grupo__nombreGrupo="2B")
    return render(request, "inicio/consultasGrupo4.html", {'tareas': tareas})


def consultarGrupo5(request):
    tareas = Tarea.objects.filter(grupo__nombreGrupo="TODOS")
    return render(request, "inicio/consultasGrupo5.html", {'tareas': tareas})
#-----------------------------------------------------------------------------


    

