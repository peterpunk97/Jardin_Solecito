# Generated by Django 5.0.6 on 2024-07-07 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_evento_grupo_tareas_grupo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tareas',
            new_name='Tarea',
        ),
    ]
