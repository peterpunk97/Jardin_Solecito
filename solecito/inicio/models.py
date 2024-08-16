from django.db import models

class Grupo(models.Model):
    idGrupo = models.AutoField(primary_key=True, verbose_name="ID GRUPO")
    nombreGrupo = models.CharField(max_length=50, verbose_name="Nombre del grupo")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ["created"]

    def __str__(self):
        return self.nombreGrupo


class Materia(models.Model):
    idMateria = models.AutoField(primary_key=True)
    nombreMateria = models.CharField(max_length=200, verbose_name="Nombre de la Materia")
    descripcionMateria = models.TextField(verbose_name="Agrega una descripción")
    imagen = models.ImageField(null=True, blank=True, upload_to="img-materias/", verbose_name="Imagen de la materia")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
        ordering = ["created"]

    def __str__(self):
        return self.nombreMateria


class Tarea(models.Model):
    idTarea = models.AutoField(primary_key=True, verbose_name="ID Tarea")
    nombreTarea = models.CharField(max_length=200, verbose_name="Nombre de la tarea")
    descripcion = models.TextField(verbose_name="Agrega una descripción")
    fechaEntrega = models.DateField(null=True, blank=True, verbose_name="Fecha de entrega")
    imagen = models.ImageField(null=True, upload_to="img-tareas", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["created"]

    def __str__(self):
        return self.nombreTarea


class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)  
    nombreEvento = models.CharField(max_length=200, verbose_name="Nombre del evento")
    fechaEvento = models.DateField(verbose_name="Fecha del evento")
    imagen = models.ImageField(null=True, blank=True, upload_to="img-eventos/", verbose_name="Imagen del evento")
    descripcion = models.TextField(verbose_name="Descripción del evento")
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["fechaEvento"]

    def __str__(self):
        return self.nombreEvento
    

class Comentario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del padre de familia")  
    correo = models.EmailField(max_length=254, verbose_name="Correo electronico")  
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefono")
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    grupos = models.CharField(max_length=4, verbose_name="Nombre del grupo") 


    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.nombre
