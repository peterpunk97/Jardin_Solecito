from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings


urlpatterns = [
    path('',views.home, name="Home"),
    path('tareas/',views.tareas, name="Tareas"),
    path('about/',views.about, name="About"),
    path('calendario/',views.calendario, name="Calendario"),
    path('contacto/',views.contacto, name="Contacto"),
    path('dudasfrecuentes/',views.dudas, name="Dudas"),
    path('admin/', admin.site.urls, name="Admin"),
    path('contacto/',views.contacto,name="Contacto"),
    path('registrar/',views.Registrar,name="Registrar"),
    path('grupo1A/',views.consultarGrupo, name="Grupo1A"),
    path('grupo1B/',views.consultarGrupo2, name="Grupo1B"),
    path('grupo2A/',views.consultarGrupo3, name="Grupo2A"),
    path('grupo2B/',views.consultarGrupo4, name="Grupo2B"),
    path('todos/',views.consultarGrupo5, name="TODOS"),
]



if settings.DEBUG:

    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)