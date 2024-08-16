from django.contrib import admin
from.models import Tarea
from.models import Grupo
from.models import Evento
from.models import Materia
from.models import Comentario



class AdministrarComentario(admin.ModelAdmin):
    readonly_fields = ('nombre', 'correo', 'telefono', 'mensaje','creado','actualizado','grupos')  
    list_display = ('nombre', 'correo', 'telefono', 'mensaje','creado','actualizado', 'grupos') 
    search_fields = ('nombre','correo', 'telefono','creado','grupos')
    list_filter = ('nombre','creado','grupos')
    list_per_page=6
admin.site.register(Comentario, AdministrarComentario)


class AdministrarTarea(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idTarea', 'nombreTarea', 'fechaEntrega','imagen',)
    search_fields = ('idTarea', 'nombreTarea', 'fechaEntrega')
    date_hierarchy = 'created'
    list_filter = ('idTarea', 'nombreTarea', 'fechaEntrega')
    list_per_page = 10
    list_display_links = ('idTarea', 'nombreTarea')
    list_editable = ('fechaEntrega',)

admin.site.register(Tarea, AdministrarTarea)


class AdministrarGrupo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idGrupo', 'nombreGrupo', 'created')
    search_fields = ('idGrupo', 'nombreGrupo', 'created')
    date_hierarchy = 'created'
    list_filter = ('idGrupo', 'nombreGrupo', 'created')
    list_per_page=5
    list_editable=('nombreGrupo',)

admin.site.register(Grupo, AdministrarGrupo)



class AdministrarEvento(admin.ModelAdmin):
    readonly_fields = ('idEvento',)  
    list_display = ('idEvento', 'nombreEvento', 'fechaEvento')
    search_fields = ('idEvento', 'nombreEvento', 'fechaEvento')
    date_hierarchy = 'fechaEvento'
    list_filter = ('fechaEvento',)
    list_per_page=5
    list_editable=('fechaEvento',)

admin.site.register(Evento, AdministrarEvento)


class AdministrarMateria(admin.ModelAdmin):
    readonly_fields = ('idMateria', 'created', 'updated')  
    list_display = ('idMateria', 'nombreMateria', 'descripcionMateria', 'created', 'updated') 
    search_fields = ('idMateria', 'nombreMateria', 'descripcionMateria')
    list_filter = ('created', 'updated')
    list_per_page=4
    list_editable=('descripcionMateria','nombreMateria')
admin.site.register(Materia, AdministrarMateria)