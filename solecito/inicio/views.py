from django.shortcuts import render

def home(request):
    return render(request, "inicio/home.html")

def about(request):
    return render(request, "inicio/about.html")

def calendario(request):
    return render(request, "inicio/calendario.html")

def tareas(request):
    return render(request, "inicio/tareas.html")

def contacto(request):
    return render(request, "inicio/contacto.html")
