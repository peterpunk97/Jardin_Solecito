from django.contrib import admin
from.models import Tarea
from.models import Grupo
from.models import Evento
from.models import Materia



class AdministrarTarea(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idTarea', 'nombreTarea', 'fechaEntrega')
    search_fields = ('idTarea', 'nombreTarea', 'fechaEntrega')
    date_hierarchy = 'created'
    list_filter = ('idTarea', 'nombreTarea', 'fechaEntrega')

admin.site.register(Tarea, AdministrarTarea)

class AdministrarGrupo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idGrupo', 'nombreGrupo', 'created')
    search_fields = ('idGrupo', 'nombreGrupo', 'created')
    date_hierarchy = 'created'
    list_filter = ('idGrupo', 'nombreGrupo', 'created')

admin.site.register(Grupo, AdministrarGrupo)


class AdministrarEvento(admin.ModelAdmin):
    readonly_fields = ('idEvento',)  
    list_display = ('idEvento', 'nombreEvento', 'fechaEvento')
    search_fields = ('idEvento', 'nombreEvento', 'fechaEvento')
    date_hierarchy = 'fechaEvento'
    list_filter = ('fechaEvento',)

admin.site.register(Evento, AdministrarEvento)


class AdministrarMateria(admin.ModelAdmin):
    readonly_fields = ('idMateria', 'created', 'updated')  
    list_display = ('idMateria', 'nombreMateria', 'descripcionMateria', 'created', 'updated') 
    search_fields = ('idMateria', 'nombreMateria', 'descripcionMateria')
    list_filter = ('created', 'updated')

admin.site.register(Materia, AdministrarMateria)
