# Generated by Django 5.0.6 on 2024-07-08 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_alter_tarea_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inicio.grupo', verbose_name='Grupo'),
        ),
    ]
