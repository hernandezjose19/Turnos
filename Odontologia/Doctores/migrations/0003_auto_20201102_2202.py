# Generated by Django 3.1 on 2020-11-02 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctores', '0002_materia_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnosasignados',
            name='ID_Turno_Disponible',
            field=models.IntegerField(unique=True),
        ),
    ]