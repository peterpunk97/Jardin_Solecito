# Generated by Django 5.0.6 on 2024-07-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_alter_grupo_options_alter_tarea_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img-tareas', verbose_name='Imagen'),
        ),
    ]
