# Generated by Django 3.1 on 2020-11-02 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctores', '0004_auto_20201102_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnosasignados',
            name='ID_Turno_Disponible',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
