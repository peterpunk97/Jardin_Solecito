# Generated by Django 5.0.6 on 2024-08-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0024_remove_tarea_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo',
            options={'ordering': ['creado'], 'verbose_name': 'Grupo', 'verbose_name_plural': 'Grupos'},
        ),
        migrations.AlterModelOptions(
            name='materia',
            options={'ordering': ['creado'], 'verbose_name': 'Materia', 'verbose_name_plural': 'Materias'},
        ),
        migrations.AlterModelOptions(
            name='tarea',
            options={'ordering': ['creado'], 'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='updated',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='created',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='materia',
            old_name='updated',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='materia',
            old_name='created',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='tarea',
            old_name='updated',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='tarea',
            old_name='created',
            new_name='creado',
        ),
        migrations.AddField(
            model_name='comentario',
            name='respuesta',
            field=models.TextField(blank=True, null=True, verbose_name='Ingresa tu respuesta'),
        ),
    ]
