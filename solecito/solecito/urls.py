from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('tareas/',views.tareas, name="Tareas"),
    path('about/',views.about, name="About"),
    path('calendario/',views.calendario, name="Calendario"),
    path('contacto/',views.contacto, name="Contacto"),
    path('admin/', admin.site.urls, name="Admin"),
]
