# Generated by Django 4.2.5 on 2023-09-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticuloDeportivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('deporte', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('valor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Univallunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('esEstudiante', models.BooleanField(default=False)),
                ('tipoDocumento', models.CharField(max_length=100)),
                ('numeroDocumento', models.CharField(max_length=100)),
                ('codigoEstudiante', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
    ]
