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
    path('admin/', admin.site.urls, name="Admin"),
]


if settings.DEBUG:

    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)