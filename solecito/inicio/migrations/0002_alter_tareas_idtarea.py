# Generated by Django 5.0.6 on 2024-07-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='idTarea',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Tarea'),
        ),
    ]
